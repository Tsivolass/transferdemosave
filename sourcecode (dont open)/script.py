import os
import json
import shutil

print('Thanks for using my mod! It\'s made in Python and is open-source. If there is any problem with the script, DM me on Discord (username: tsivolass) or email me at devtsivolass@gmail.com.')

num = input('old save number: ')
nun = input('New save number: ')
num1 = int(num)
nun1 = int(nun)
if nun1 > 5 or num1 > 5:
    exit()
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

def copy_business_files(source_folder, target_folder):
    """Copy all files from source to target."""
    if not os.path.exists(source_folder):
        print(f"Warning: Source folder {source_folder} does not exist. Skipping.")
        return
    os.makedirs(target_folder, exist_ok=True)
    for file_name in os.listdir(source_folder):
        source_file = os.path.join(source_folder, file_name)
        target_file = os.path.join(target_folder, file_name)
        if os.path.isfile(source_file):
            shutil.copy2(source_file, target_file)
            print(f'Copied {file_name} to {target_folder}')

# Base directory for saves
tempbase_directory = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I', 'Saves')

oldsavespath = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I Free Sample', 'Saves', f'SaveGame_{num}')
newtemp = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I', 'saves')



for filename in os.listdir(tempbase_directory):
    irectory = f'{tempbase_directory}\\{filename}\\SaveGame_{nun}'
    if os.path.exists(irectory):
        print(f'new save: SaveGame_{nun} already exists')
        exit()
    else:
        
        
        os.rename(oldsavespath, irectory)
        base_directory = os.path.join(tempbase_directory, filename, f'SaveGame_{nun}')
    break  # Ensure we use the first valid directory


# Copy Post Office separately
postpath = "C:\Program Files (x86)\Steam\steamapps\common\Schedule I\Schedule I_Data\StreamingAssets\DefaultSave\Businesses"

targetfolder = os.path.join(base_directory, "Businesses")
 # Remove the target folder if it already exists
if os.path.exists(targetfolder):
        shutil.rmtree(targetfolder)  # Remove the target folder if it already exists
    
shutil.copytree(postpath, targetfolder)
print(f'Copied {postpath} to {targetfolder}')



oldsavespath = os.path.join(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'TVGS', 'Schedule I Free Sample', 'Saves', f'SaveGame_{num}')


version = '0.3.3f14'

movedirec = os.path.join(base_directory)

shutil.move(oldsavespath, movedirec)
print(f'Moved {oldsavespath} to {base_directory}')
changeversion(movedirec, version)

print("All files copied successfully!")


