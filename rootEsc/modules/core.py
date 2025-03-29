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
white=Fore.WHITE
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
    
    def user_enumerator(self):
        all_folders=sorted(load_folders(SCRIPTS_DIR))
        user_analysis_dir = all_folders[2]
        scripts = sorted(load_files(SCRIPTS_DIR + user_analysis_dir + "/"))
        print("     ---===::: User enumeration started :::===---    ")
        # TODO : uncomment it after adding files in scripts folder.
        # for script in scripts:
        #     run_command(SCRIPTS_DIR + user_analysis_dir + "/" + script)
        
    def system_enumerator(self):
        all_folders=sorted(load_folders(SCRIPTS_DIR))
        system_analysis_dir = all_folders[0]
        scripts = sorted(load_files(SCRIPTS_DIR + system_analysis_dir + "/"))
        print("     ---===::: System enumeration started :::===---    ")
        for script in scripts:
            print(f"Running script : {script}")
            run_command(SCRIPTS_DIR + system_analysis_dir + "/" + script)
    
    def files_enumerator(self):
        all_folders=sorted(load_folders(SCRIPTS_DIR))
        files_analysis_dir = all_folders[1]
        scripts = sorted(load_files(SCRIPTS_DIR + files_analysis_dir + "/"))
        print("     ---===::: files enumeration started :::===---    ")
        for script in scripts:
            print(f"Running script : {script}")
            run_command(SCRIPTS_DIR + files_analysis_dir + "/" + script)
        
    def core_handler(self):
        if not (self.cli.args().no_colours):
            print(self.cli.banner())
        end_time=perf_counter()
        self.system_enumerator()
        self.files_enumerator()
        self.user_enumerator()
        print(f"Time taken to complete : {end_time-start_time}")
        #print(self.file_analysis.get_writable_permission_dirs_in_env_path().stdout)
        
    def start(self):
        self.core_handler()
        
if __name__ == "__main__":
    core=RootEscCore()
    core.core_handler()
