import os
import json
import shutil
print('Thanks for using my mod! Its made in python and its opensource. If there is any problem with the script, dm me on discord (username: tsivolass) or to my email (devtsivolass@gmail.com).')
num = input('Old save number: ')
nun = input('New save number: ')

def changeversion(path):
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

# Define old and new save paths
oldsavepath = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I Free Sample', 'saves', f'SaveGame_{num}')
newtemp = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I', 'saves')

# Find the correct new save location
for foldername in os.listdir(newtemp):
    newsaveloc = os.path.join(newtemp, foldername)
    newsavepath = os.path.join(newsaveloc, f'SaveGame_{nun}')
    fisse_path = os.path.join(newsavepath, 'Money.json')
    with open(fisse_path, 'r') as file:
                    data = json.load(file)
                    print(f'Opened ')
    version = data['GameVersion']
    if os.path.exists(newsavepath):
        print(f'SaveGame_{nun} already exists. Exiting.')
        exit()
    else:
        # Move the old save to the new location
        shutil.move(oldsavepath, newsavepath)
        print(f'Moved {oldsavepath} to {newsavepath}')

        # Update all JSON files in the new save folder
        changeversion(newsavepath)
