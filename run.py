import re
import requests
import json
import subprocess
import os


def download_file(url, file_name):
    try:
        # Make GET request
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        # Save the content to a file
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return file_name
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading {file_name}: {e}")
        return None


def extract_uris(data):
    """Recursive function to extract 'uri' values from a JSON object."""
    uris = []
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "uri":
                uris.append(value)
            else:
                uris.extend(extract_uris(value))
    elif isinstance(data, list):
        for item in data:
            uris.extend(extract_uris(item))
    return uris


def main():
    input_user = input("Enter Vectary URL: ")
    pattern = r"(?<=model=)[a-f0-9\-]+"

    match = re.search(pattern, input_user)
    if match:
        model_id = match.group(0)
        print("ID found:", model_id)

        # Download the .gltf model
        file_name = download_file(f"https://app.vectary.com/viewer/data/{model_id}/gltf/{model_id}.gltf", f"{model_id}.gltf")
        if not file_name:
            return

        # Load the JSON file
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Extract all "uri" values
        all_uris = extract_uris(data)
        print(f"Downloading the necessary files...")

        # Download all files related to the URIs
        for uri in all_uris:
            download_file(f"https://app.vectary.com/viewer/data/{model_id}/gltf/{uri}", uri)

        # Run the conversion with gltf-pipeline
        command = ["gltf-pipeline", "-i", file_name, "-o", f"{model_id}.glb"]
        subprocess.run(command)

        # Clean up the temporary files
        for uri in all_uris:
            os.remove(uri)
        os.remove(file_name)

    else:
        print("No ID found.")


if __name__ == "__main__":
    main()
