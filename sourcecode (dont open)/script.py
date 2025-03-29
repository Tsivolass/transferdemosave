import os
import requests
import zipfile
import io
gamesavenumber = input('Game save number: ')
def download_and_extract_zip(url, destination_folder):
    """Downloads a ZIP file from a given URL and extracts it to the destination folder."""
    os.makedirs(destination_folder, exist_ok=True)  # Ensure folder exists
    
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(destination_folder)
        print(f"Extracted ZIP from {url} to {destination_folder}")
    else:
        print(f"Failed to download {url}")

# Base directory (Change this to the correct path)
tempbase_directory = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I', 'saves')

for filename in os.listdir(tempbase_directory):
    base_directory = os.path.join(tempbase_directory, filename, f'SaveGame_{gamesavenumber}')

# List of business subfolders and corresponding GitHub ZIP file URLs
business_folders = {
    "Taco Ticklers": "https://github.com/Tsivolass/assets/blob/main/launderingstation_6e6751.zip",
    "Post Office": "https://github.com/Tsivolass/assets/blob/main/launderingstation_ad5374.zip",
    "Car Wash": "https://github.com/Tsivolass/assets/blob/main/launderingstation_9e5c54.zip",
    "Laundromat": "https://github.com/Tsivolass/assets/blob/main/launderingstation_8ffd1d.zip"
}

# Iterate through the folders and download/extract ZIP files
for business, url in business_folders.items():
    target_folder = os.path.join(base_directory, "Businesses", business, "Objects")
    download_and_extract_zip(url, target_folder)

print("All downloads and extractions completed!")
