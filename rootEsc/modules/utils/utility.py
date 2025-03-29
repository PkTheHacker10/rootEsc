try:
    import os
    import subprocess

except ImportError as Ie:
    print(f"Error [Utility] : {Ie}")


def load_folders(path):
    # Function to load the files by the given path.
    files_and_folders=os.listdir(path)
    all_folders=[]

    # Extraction only files from listdir. 
    for folder in files_and_folders:
        # Checking whether it is a file or a folder.
        if os.path.isfile(folder + folder):
            continue
        else:
            all_folders.append(folder)
    return all_folders

def load_files(folder):
    # Function to load all the folders by the given path.
    files_and_folders=os.listdir(folder)
    all_files=[]

    # Extraction only files from listdir. 
    for file in files_and_folders:
        # Checking whether it is a file or a folder.
        if os.path.isfile(folder + file):
            all_files.append(file)
    return all_files

def get_current_working_dir():
    # Function to get current working directory.
    return os.getcwd()

def run_command(command):
    # Function to Run a command.
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout.strip())
