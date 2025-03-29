try:
    from time import perf_counter
    from colorama import Fore,Style
    from modules.cli.cli import CommandLine
    from modules.analyzers.file import FileAnalysis
    from modules.analyzers.system import SystemAnalysis
    
    
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

class RootEscCore():
    def __init__(self):
        self.cli = CommandLine()
        self.file_analysis = FileAnalysis()
        self.system_analysis = SystemAnalysis()
    
    def user_privilege_enumerator(self):
        pass
        
    
    def system_enumerator(self):
        pass
    
    def files_enumerator(self):
        pass
        
    def core_handler(self):
        if not (self.cli.args().no_colours):
            print(self.cli.banner())
        end_time=perf_counter()
        print(f"Time taken to complete : {end_time-start_time}")
        #print(self.file_analysis.get_writable_permission_dirs_in_env_path().stdout)
        
    def start(self):
        self.core_handler()
        
if __name__ == "__main__":
    core=RootEscCore()
    core.core_handler()
