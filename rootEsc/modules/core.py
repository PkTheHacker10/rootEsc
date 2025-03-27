try:
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
        user_privilege_result="""{green}[ ✓ ]{reset}{blue} User id : {reset}\n{id}\n{green}[ ✓ ]{reset}{blue} User sudo privilege (sudo -l) :{reset} \n\n{sudo_privilege_test}{reset}{green}[ ✓ ]{reset}{blue} All users: {reset}\n{all_users}\n\n{green}[ ✓ ]{reset}{blue} All root users: {reset}\n{root_users}"""
        user_id=self.user_analysis.get_current_user_id().stdout
        sudo_privilege_test=self.user_analysis.get_sudo_privileges().stdout
        all_users=self.user_analysis.get_all_users().stdout.strip()
        root_users=self.user_analysis.get_all_root_users().stdout
        
        return user_privilege_result.format(id=user_id,sudo_privilege_test=sudo_privilege_test,yellow=yellow,reset=reset,blue=blue,all_users=all_users,root_users=root_users,green=green)
    
    def system_enumerator(self):
        system_enumerator_result="""{green}\n[ ✓ ]{reset}{blue} Kernal information : {reset}\n{kernal_info}{reset}\n{green}[ ✓ ] {reset}{blue}Sudo version :\n{reset}{sudo_version}\n{green}[ ✓ ]{reset}{blue} Capabilities Inforamation : {reset}\n{capabilities_info} \n\n{green}[ ✓ ]{reset}{blue} Crontab taskes : {reset}{crontabs_info}"""
        kernal_info = self.system_analysis.get_kernel_info().stdout
        sudo_version = self.system_analysis.get_sudo_version().stdout
        capabilities_info = self.system_analysis.get_capabilities().stdout
        crontabs_info = self.system_analysis.get_crontabs_tasks().stdout
        return system_enumerator_result.format(green=green,blue=blue,kernal_info=kernal_info,reset=reset,sudo_version=sudo_version,capabilities_info=capabilities_info,crontabs_info=crontabs_info)
    
    def process_enumerator(self):
        pass
    
    def logs_enumerator(self):
        pass
    
    def files_enumerator(self):
        file_enumerator_result="""{green}[ ✓ ]{reset}{blue} SUID Binary : {reset}\n{suid_binary}{reset}\n{green}[ ✓ ] {reset}{blue}SGID Binary : {reset}\n{sgid_binary}\n[ ✓ ] {reset}{blue} Writable Env PATH :{reset}\n{writable_env_path}"""
        suid_bins=self.file_analysis.get_suid_bins().stdout
        sgid_bins=self.file_analysis.get_sgid_bins().stdout
        writable_env_path=self.file_analysis.get_writable_permission_dirs_in_env_path().stdout
        return file_enumerator_result.format(green=green,blue=blue,suid_binary=suid_bins,sgid_binary=sgid_bins,writable_env_path=writable_env_path,reset=reset)
        
    def core_handler(self):
        arguments=self.cli.args()
        
        if not (arguments.no_colours):
            banner=self.cli.banner()
            print(banner)
            
        user_analysis=self.user_privilege_enumerator()
        system_analysis=self.system_enumerator()
        file_analysis=self.files_enumerator()
        print(system_analysis)
        print(user_analysis)
        print(file_analysis)
        #print(self.file_analysis.get_writable_permission_dirs_in_env_path().stdout)
        
    
    def start(self):
        self.core_handler()
        
        
if __name__ == "__main__":
    core=RootEscCore()
    core.core_handler()