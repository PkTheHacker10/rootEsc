try:
    from time import sleep
    from threading import Thread
    from modules.cli.cli import CommandLine
    from modules.analyzers.file import FileAnalysis
    from modules.analyzers.logs import LogAnalysis
    from modules.analyzers.process import ProcessAnalysis
    from modules.analyzers.system import SystemAnalysis
    from modules.analyzers.user import UserAnalysis
    from colorama import Fore,Style
    
except ImportError as Ie:
    print(f"Error [Core] : {Ie}")
 

red=Fore.RED
blue=Fore.BLUE
white=Fore.WHITE
magenta=Fore.MAGENTA
bright=Style.BRIGHT
green=Fore.GREEN
red=Fore.RED
bold=Style.BRIGHT
yellow=Fore.YELLOW
cyan=Fore.CYAN
mixed=Fore.BLUE+Fore.GREEN+Fore.RED
reset=Style.RESET_ALL

class RootEscCore():
    def __init__(self):
        self.cli = CommandLine()
        self.file_analysis = FileAnalysis()
        self.log_analysis = LogAnalysis()
        self.process_analysis = ProcessAnalysis()
        self.system_analysis = SystemAnalysis()
        self.user_analysis = UserAnalysis()
    
    def user_privilege_enumerator(self):
        user_privilege_result="""{green} [ ✓ ] User id : {id}{reset}{green} [ ✓ ] User sudo privilege (sudo -l) : {sudo_privilege_test} {reset}{blue}\n [ → ] Trying to enumerate all users...{reset}\n{all_users}\n\n{green}[ ✓ ] All users enumerated ...{reset}\n{blue}[ ! ] Trying to enumerate root users...{reset}\n\n{root_users}"""
        user_id=self.user_analysis.get_current_user_id().stdout.decode()
        sudo_privilege_test=self.user_analysis.get_sudo_privileges().stdout.decode()
        all_users=self.user_analysis.get_all_users().stdout.decode()
        root_users=self.user_analysis.get_all_root_users().stdout.decode()
        
        return user_privilege_result.format(id=user_id,sudo_privilege_test=sudo_privilege_test,yellow=yellow,reset=reset,blue=blue,all_users=all_users,root_users=root_users,green=green)
    
    def system_enumerator(self):
        pass
    
    def process_enumerator(self):
        pass
    
    def logs_enumerator(self):
        pass
    
    def files_enumerator(self):
        pass
        
    def core_handler(self):
        banner=self.cli.banner()
        print(banner)
        user_analysis=self.user_privilege_enumerator()
        print(user_analysis)
        #print(f"[ + ] All users in the system :-\n\n{self.user_analysis.get_all_users(index=1).stdout.decode()}")
    
    def start(self):
        self.core_handler()
        
        
if __name__ == "__main__":
    core=RootEscCore()
    core.core_handler()