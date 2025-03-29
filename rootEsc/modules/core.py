try:
    from time import perf_counter
    from colorama import Fore,Style
    from modules.cli.cli import CommandLine
    from modules.utils.utility import load_files,load_folders,run_command,get_current_working_dir
    
except ImportError as Ie:
    print(f"Error [Core] : {Ie}")
 
start_time=perf_counter()

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
            print(f"Unexpected Error [Core.user_enumerator] : {Ue}")
    
    def files_enumerator(self):
        all_folders=sorted(load_folders(SCRIPTS_DIR))
        files_analysis_dir = all_folders[1]
        scripts = sorted(load_files(SCRIPTS_DIR + files_analysis_dir + "/"))
        print(f"\n{blue}       ═══════════════{reset} Files enumeration started {blue}═══════════════{reset}")
        for script in scripts:
            print(f"{green}\n[ ✓ ]{reset} Enumerating {script.split(".")[0].split("_")[1]} :")
            run_command(SCRIPTS_DIR + files_analysis_dir + "/" + script)
        
    def core_handler(self):
        end_time=perf_counter()
        self.system_enumerator()
        self.files_enumerator()
        print(f"Time taken to complete : {end_time-start_time}")

    def start(self):
        self.core_handler()
        
if __name__ == "__main__":
    core=RootEscCore()
    core.core_handler()
