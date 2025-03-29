try:
    from colorama import Fore,Style
    from modules.cli.cli import CommandLine
    from modules.utils.utility import load_files,load_folders,run_command,get_current_working_dir
    
except ImportError as Ie:
    print(f"Error [Core] : {Ie}")

red=Fore.RED
green=Fore.GREEN
blue=Fore.BLUE
red=Fore.RED
bold=Style.BRIGHT
yellow=Fore.YELLOW
reset=Style.RESET_ALL

SCRIPTS_DIR = get_current_working_dir() + "/modules/scripts/"

class RootEscCore():
    def __init__(self):
        self.cli = CommandLine()
        
    def system_enumerator(self):
        try:
            all_folders=sorted(load_folders(SCRIPTS_DIR))
            system_analysis_dir = all_folders[0]
            scripts = sorted(load_files(SCRIPTS_DIR + system_analysis_dir + "/"))
            print(f"\n{blue}       ═══════════════{reset} System enumeration started {blue}═══════════════{reset}")
            for script in scripts:
                print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
                run_command(SCRIPTS_DIR + system_analysis_dir + "/" + script)

        except Exception as Ue:
            print(f"{red}[ ! ]{reset} Unexpected Error [Core.system_enumerator] : {Ue}")
    
    def files_enumerator(self):
        try:
            all_folders=sorted(load_folders(SCRIPTS_DIR))
            files_analysis_dir = all_folders[1]
            scripts = sorted(load_files(SCRIPTS_DIR + files_analysis_dir + "/"))
            print(f"\n{blue}       ═══════════════{reset} Files enumeration started {blue}═══════════════{reset}")
            for script in scripts:
                print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
                run_command(SCRIPTS_DIR + files_analysis_dir + "/" + script)

        except Exception as Ue:
            print(f"{red}[ ! ]{reset} Unexpected Error [Core.file_enumerator] : {Ue}")

    def process_enumerator(self):
        try:
            all_folders=sorted(load_folders(SCRIPTS_DIR))
            process_analysis_dir = all_folders[2]
            scripts = sorted(load_files(SCRIPTS_DIR + process_analysis_dir + "/"))
            print(f"\n{blue}       ═══════════════{reset} Process enumeration started {blue}═══════════════{reset}")
            for script in scripts:
                print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
                run_command(SCRIPTS_DIR + process_analysis_dir + "/" + script)
        except Exception as Ue:
            print(f"{red}[ ! ]{reset} Unexpected Error [Core.process_enumerator] : {Ue}")

    def network_enumerator(self):
        try:
            all_folders=sorted(load_folders(SCRIPTS_DIR))
            network_analysis_dir = all_folders[3]
            scripts = sorted(load_files(SCRIPTS_DIR + network_analysis_dir + "/"))
            print(f"\n{blue}       ═══════════════{reset} Network enumeration started {blue}═══════════════{reset}")
            for script in scripts:
                print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
                run_command(SCRIPTS_DIR + network_analysis_dir + "/" + script)

        except Exception as Ue:
            print(f"{red}[ ! ]{reset} Unexpected Error [Core.network_enumerator] : {Ue}")

    def log_enumerator(self):
        try:
            all_folders=sorted(load_folders(SCRIPTS_DIR))
            log_analysis_dir = all_folders[4]
            scripts = sorted(load_files(SCRIPTS_DIR + log_analysis_dir + "/"))
            print(f"\n{blue}       ═══════════════{reset} Log enumeration started {blue}═══════════════{reset}")
            for script in scripts:
                print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
                run_command(SCRIPTS_DIR + log_analysis_dir + "/" + script)
        except Exception as Ue:
            print(f"{red}[ ! ]{reset} Unexpected Error [Core.log_enumerator] : {Ue}")
        
    def core_handler(self):
        self.system_enumerator()
        self.files_enumerator()
        self.process_enumerator()
        self.network_enumerator()
        self.log_enumerator()

    def start(self):
        self.core_handler()
        
