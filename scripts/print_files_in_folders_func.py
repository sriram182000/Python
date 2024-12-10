import os

def get_files(folder):
    try:
        files=os.listdir(folder)
        return files,None
    except FileNotFoundError:
        return None, "Files not found"


def get_folders():
    folders_paath = input("Enter the folder names with space separated in between: ").split()

    for folder in folders_paath:
        files,error_message=get_files(folder)
        if files:
            print(f"Files in {folder} are: ")
            for file in files:
                print(file)
        else:
            print(f"{folder} is not a valid folder - {error_message}")
            break
get_folders()
