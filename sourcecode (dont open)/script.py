import os
import requests
import zipfile
import io
import json
import shutil

print('Thanks for using my mod! It\'s made in Python and is open-source. If there is any problem with the script, DM me on Discord (username: tsivolass) or email me at devtsivolass@gmail.com.')

num = input('Old save number: ')
nun = input('New save number: ')

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

def changeversion(path, version):
    """Update the GameVersion in all JSON files within the specified directory."""
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        
        if file_name.endswith('.json') and os.path.isfile(file_path):
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    print(f'Opened {file_name}')
                
                # Update GameVersion
                data["GameVersion"] = version

                # Save the modified data back
                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)
                    print(f'Updated {file_name}')
            except json.JSONDecodeError as e:
                print(f'Error decoding {file_name}: {e}')
            except IOError as e:
                print(f'File error with {file_name}: {e}')

# Base directory for downloading files
tempbase_directory = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I', 'saves')

for filename in os.listdir(tempbase_directory):
    base_directory = os.path.join(tempbase_directory, filename, f'SaveGame_{nun}')
oldsavepath = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I Free Sample', 'saves', f'SaveGame_{num}')
newtemp = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I', 'saves')
# Find the correct new save location
for foldername in os.listdir(newtemp):
    newsaveloc = os.path.join(newtemp, foldername)
    newsavepath = os.path.join(newsaveloc, f'SaveGame_{nun}')
    fisse_path = os.path.join(newsavepath, 'Money.json')
    
    version = '0.3.3f13'
    
    if os.path.exists(newsavepath):
        print(f'SaveGame_{nun} already exists. Exiting.')
        exit()
    else:
        # Move the old save to the new location
        shutil.move(oldsavepath, newsavepath)
        print(f'Moved {oldsavepath} to {newsavepath}')

        # Update all JSON files in the new save folder
        changeversion(newsavepath, version)

# List of business subfolders and corresponding GitHub ZIP file URLs
business_folders = {
    "Taco Ticklers": "https://github.com/Tsivolass/assets/raw/main/launderingstation_6e6751.zip",
    "Post Office": "https://github.com/Tsivolass/assets/raw/main/launderingstation_ad5374.zip",
    "Car Wash": "https://github.com/Tsivolass/assets/raw/main/launderingstation_9e5c54.zip",
    "Laundromat": "https://github.com/Tsivolass/assets/raw/main/launderingstation_8ffd1d.zip"
}

# Iterate through the folders and download/extract ZIP files
for business, url in business_folders.items():
    target_folder = os.path.join(base_directory, "Businesses", business, "Objects")
    download_and_extract_zip(url, target_folder)

print("All downloads and extractions completed!")

# Define old and new save paths



