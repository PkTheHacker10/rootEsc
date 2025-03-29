try:
    import os
    import subprocess

except ImportError as Ie:
    print(f"Error [Utility] : {Ie}")

def load_folders(path):
    files_and_folders=os.listdir(path)
    all_folders=[]
    for folder in files_and_folders:
        if os.path.isfile(folder + folder):
            continue
        else:
            all_folders.append(folder)
    return all_folders

def load_files(folder):
    files_and_folders=os.listdir(folder)
    all_files=[]
    for file in files_and_folders:
        if os.path.isfile(folder + file):
            all_files.append(file)
    return all_files

def get_current_working_dir():
    return os.getcwd()

def run_command(command):
    """ Runs a command and returns the formatted output """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout.strip())
