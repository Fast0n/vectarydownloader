# Vectary Downloader

This script allows you to download a 3D model from Vectary and convert it to the `.gltf` format using the `gltf-pipeline` command.

## How it works

1. **Enter the Vectary model URL**: The script extracts the model ID from the provided URL.
2. **Download the model**: The model in `.gltf` format is downloaded along with all necessary files indicated by the URIs in the JSON file.
3. **Merging**: All files are combined to recreate the `.gltf` file.
4. **Cleanup**: Temporary files are deleted after the operation is completed.

## Prerequisites

- Python 3.x
- Poetry for managing dependencies.
- `gltf-pipeline` for converting the model:
   ```bash 
   npm install -g gltf-pipeline

## Setting up the project

1. Clone or download this repository.
2. Install Poetry (if not already installed). You can follow the installation instructions on the official Poetry website: https://python-poetry.org/docs/#installation
3. Install the required dependencies by running:
   ```bash
   poetry install --no-root

## Example Vectary model URL

https://www.vectary.com/viewer/v1/?model=73e4e032-a0d1-4440-99c0-155856c6b30d&env=studio3&turntable=3