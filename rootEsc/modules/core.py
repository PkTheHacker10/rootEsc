try:
    from colorama import Fore,Style
    from modules.cli.cli import CommandLine
    from modules.utils.utility import load_files,load_folders,run_command,get_current_working_dir
    
except ImportError as Ie:
    print(f"Error [Core] : {Ie}")

red=Fore.RED
green=Fore.GREEN
blue=Fore.BLUE
bold=Style.BRIGHT
yellow=Fore.YELLOW
reset=Style.RESET_ALL

# Path to the scripts.
SCRIPTS_DIR = get_current_working_dir() + "/modules/scripts/"

class RootEscCore():
    # Class to manage the rootESC.
    def __init__(self):
        self.cli = CommandLine()
        
    def system_enumerator(self):
        # Function to handle system enumeration.
        try:
            # Getting all folders from scrips directory.
            all_folders=sorted(load_folders(SCRIPTS_DIR))
            # Specifying system enumeration script directory [ 0 = 1_system ]
            system_analysis_dir = all_folders[0]
            # Gathering all scripts that is inside in the scripts/1_system directory. 
            scripts = sorted(load_files(SCRIPTS_DIR + system_analysis_dir + "/"))
            print(f"\n{blue}       ═══════════════{reset} System enumeration started {blue}═══════════════{reset}")
            
            # Executing all the scripts that is inside in the scripts/1_system one by one.
            for script in scripts:
                print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
                run_command(SCRIPTS_DIR + system_analysis_dir + "/" + script)

        except Exception as Ue:
            print(f"{red}[ ! ]{reset} Unexpected Error [Core.system_enumerator] : {Ue}")
    
    def files_enumerator(self):
        # Function to handle file enumeration.
        try:
            # Getting all folders from scrips directory.
            all_folders=sorted(load_folders(SCRIPTS_DIR))
            # Specifying file enumeration script directory [ 1 = 2_files ]
            files_analysis_dir = all_folders[1]
            # Gathering all scripts that is inside in the scripts/2_files directory.
            scripts = sorted(load_files(SCRIPTS_DIR + files_analysis_dir + "/"))
            print(f"\n{blue}       ═══════════════{reset} Files enumeration started {blue}═══════════════{reset}")

            # Executing all the scripts that is inside in the scripts/1_files one by one.
            for script in scripts:
                print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
                run_command(SCRIPTS_DIR + files_analysis_dir + "/" + script)

        except Exception as Ue:
            print(f"{red}[ ! ]{reset} Unexpected Error [Core.file_enumerator] : {Ue}")

    def process_enumerator(self):
        # Function to handle process enumeration.
        try:
            # Getting all folders from scrips directory.
            all_folders=sorted(load_folders(SCRIPTS_DIR))
            # Specifying process enumeration script directory [ 2 = 3_process ]
            process_analysis_dir = all_folders[2]
            # Gathering all scripts that is inside in the scripts/3_process directory.
            scripts = sorted(load_files(SCRIPTS_DIR + process_analysis_dir + "/"))
            print(f"\n{blue}       ═══════════════{reset} Process enumeration started {blue}═══════════════{reset}")

            # Executing all the scripts that is inside in the scripts/2_process one by one.
            for script in scripts:
                print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
                run_command(SCRIPTS_DIR + process_analysis_dir + "/" + script)

        except Exception as Ue:
            print(f"{red}[ ! ]{reset} Unexpected Error [Core.process_enumerator] : {Ue}")

    def network_enumerator(self):
        # Function to handle network enumeration.
        try:
            # Getting all folders from scrips directory.
            all_folders=sorted(load_folders(SCRIPTS_DIR))
            # Gathering all scripts that is inside in the scripts/4_network directory.
            network_analysis_dir = all_folders[3]
            # Specifying system enumeration script directory [ 3 = 4_process ]
            scripts = sorted(load_files(SCRIPTS_DIR + network_analysis_dir + "/"))
            print(f"\n{blue}       ═══════════════{reset} Network enumeration started {blue}═══════════════{reset}")
            
            # Executing all the scripts that is inside in the scripts/4_network one by one.
            for script in scripts:
                print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
                run_command(SCRIPTS_DIR + network_analysis_dir + "/" + script)

        except Exception as Ue:
            print(f"{red}[ ! ]{reset} Unexpected Error [Core.network_enumerator] : {Ue}")

    def log_enumerator(self):
        # Function to handle log enumertaion. 
        try:
            # Getting all folders from scrips directory.
            all_folders=sorted(load_folders(SCRIPTS_DIR))
            # Specifying system enumeration script directory [ 4 = 5_log ]
            log_analysis_dir = all_folders[4]
            # Executing all the scripts that is inside in the scripts/5_log one by one.
            scripts = sorted(load_files(SCRIPTS_DIR + log_analysis_dir + "/"))
            print(f"\n{blue}       ═══════════════{reset} Log enumeration started {blue}═══════════════{reset}")

            # Executing all the scripts that is inside in the scripts/5_log one by one.
            for script in scripts:
                print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
                run_command(SCRIPTS_DIR + log_analysis_dir + "/" + script)

        except Exception as Ue:
            print(f"{red}[ ! ]{reset} Unexpected Error [Core.log_enumerator] : {Ue}")
        
    def core_handler(self):
        # Function to handle all the enumerators.
        self.system_enumerator()
        self.files_enumerator()
        self.process_enumerator()
        self.network_enumerator()
        self.log_enumerator()

    def start(self):
        # Funtion that start the core handler function. 
        self.core_handler()
        
