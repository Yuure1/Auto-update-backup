import os 
import shutil 
import time

folderPath = "C:/Users/MrRobot/Desktop/portfolio - Copy"
backupPath = "C:/Users/MrRobot/Desktop/New folder"

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
    
def checkTypeAndCopy(x, y):
    if os.path.isfile(x):
        if shutil.copy2(x, y):
            return True
        
    elif os.path.isdir(x):
        print(x)
        print(y)
        if shutil.copytree(x, y):
            return True
    
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
        if checkTypeAndCopy(ftcPath, dPath):
            print(f'"{fileToCopy[i]}"' + " is now up to date.")
            print("")

def backupNewFile(fileToBackup):
    ftbPath = os.path.join(folderPath, fileToBackup)
    print(f'"{fileToBackup}"' + " hasn't been backed up.")
    print("Backing up " + f'"{fileToBackup}"' + "...")
    if checkTypeAndCopy(ftbPath, backupPath + "/" + fileToBackup): # change path
        print("Success!")
        print("")

# END OF METHODS


while True:
    backupDone = False
    if not backupDone:
        if exists(folderPath) and exists(backupPath): # If both directories exist/are valid
            folderFiles = os.listdir(folderPath) # List the content of both directories
            backupFiles = os.listdir(backupPath)
            fileCount = len(folderFiles) # Get file count
            
            if folderFiles == backupFiles: # Check if both directories have the same content
                for i in range(fileCount):
                    checkModDateAndSize(folderFiles, backupFiles, i)
            # If directory content is not the same
            else: 
                for i in folderFiles:
                    if i not in backupFiles: # Look for files missing in the backup folder & back them up
                        backupNewFile(i)
                        
    backupDone = True
    if backupDone:
        print("")
        print("Backup folder is up to date!!")
    time.sleep(10)