import os 
import shutil 

folderPath = "fold"
backupPath = "fold_backup"

def exists(path):
    if os.path.exists(path) and os.path.isdir(path): # Check if path exists and is a directory
        print(str(path) + " - is a path and a directory")
        return True
    elif os.path.isfile(path):
        print(str(path) + " - is a file and not a folder.") # Not a directory
        return False
    elif not os.path.exists(path):
        print(str(path) + " - is invalid or does not exist.") # Invalid path given
        return False
    
def checkModDateAndSize(fileToCopy, dest, i):
    ftcPath = os.path.join(folderPath, fileToCopy[i])
    dPath = os.path.join(backupPath, dest[i])

    ftcModTime = os.path.getmtime(ftcPath)
    dModTime = os.path.getmtime(dPath)

    ftcSize = os.path.getsize(ftcPath)
    dSize = os.path.getsize(dPath)

    if (ftcModTime != dModTime) or (ftcSize != dSize):
        print(f'"{fileToCopy[i]}"' + " is out of date.")
        print("Updating " + f'"{fileToCopy[i]}"' + "...")
        shutil.copy(ftcPath, dPath) # Copy file
        shutil.copystat(ftcPath, dPath) # Copy file metadata
        print(f'"{fileToCopy[i]}"' + " is now up to date.")
        print("")

def backupNewFile(fileToBackup):
    ftbPath = os.path.join(folderPath, fileToBackup)
    print(f'"{fileToBackup}"' + " hasn't been backed up.")
    print("Backing up " + f'"{fileToBackup}"' + "...")
    shutil.copy(ftbPath, backupPath)
    print("Success!")
    print("")

# END OF METHODS

if exists(folderPath) and exists(backupPath):
    folderFiles = os.listdir(folderPath)
    backupFiles = os.listdir(backupPath)
    fileCount = len(folderFiles)

    if folderFiles == backupFiles: # Check if both directories have the same content
        for i in range(fileCount):
            checkModDateAndSize(folderFiles, backupFiles, i)
    # If directory content is not the same
    else: 
        for i in folderFiles:
            if i not in backupFiles: # Look for files missing in the backup folder & back them up
                backupNewFile(i)