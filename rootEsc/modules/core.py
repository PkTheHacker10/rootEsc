try:
    from time import perf_counter
    from colorama import Fore,Style
    from concurrent.futures import ProcessPoolExecutor
    from modules.cli.cli import CommandLine
    from modules.analyzers.file import FileAnalysis
    from modules.analyzers.logs import LogAnalysis
    from modules.analyzers.process import ProcessAnalysis
    from modules.analyzers.system import SystemAnalysis
    from modules.analyzers.user import UserAnalysis
    
    
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
        self.log_analysis = LogAnalysis()
        self.process_analysis = ProcessAnalysis()
        self.system_analysis = SystemAnalysis()
        self.user_analysis = UserAnalysis()
    
    def user_privilege_enumerator(self):
        user_id=self.user_analysis.get_current_user_id().stdout.strip()
        sudo_privilege_test=self.user_analysis.get_sudo_privileges().stdout.strip()
        all_users=self.user_analysis.get_all_users().stdout.strip()
        root_users=self.user_analysis.get_all_root_users().stdout.strip()
        
        return {
            "user_id":user_id,
            "sudo_privilege_test":sudo_privilege_test,
            "all_users":all_users,
            "root_users":root_users
        }
        
    
    def system_enumerator(self):
        kernal_info = self.system_analysis.get_kernel_info().stdout.strip()
        sudo_version = self.system_analysis.get_sudo_version().stdout.strip()
        capabilities_info = self.system_analysis.get_capabilities().stdout.strip()
        crontabs_info = self.system_analysis.get_crontabs_tasks().stdout.strip()
        
        return {
            "kernal_info":kernal_info,
            "sudo_version":sudo_version,
            "capabilities_info":capabilities_info,
            "crontabs_info":crontabs_info
        }
        
    def process_enumerator(self):
        pass
    
    def logs_enumerator(self):
        pass
    
    def files_enumerator(self):
        suid_bins=self.file_analysis.get_suid_bins().stdout.strip()
        sgid_bins=self.file_analysis.get_sgid_bins().stdout.strip()
        writable_env_path=self.file_analysis.get_writable_permission_dirs_in_env_path().stdout.strip()
        return {
            "suid_bins":suid_bins,
            "sgid_bins":sgid_bins,
            "writable_env_path":writable_env_path
        }
        
    def core_handler(self):
        if not (self.cli.args().no_colours):
            print(self.cli.banner())
            
        with ProcessPoolExecutor() as executor:
            futures = {
                "user_analysis": executor.submit(self.user_privilege_enumerator),
                "system_analysis": executor.submit(self.system_enumerator),
                "file_analysis": executor.submit(self.files_enumerator),
            }

        results = {key: future.result() for key, future in futures.items()}
        output = f"""
{green}\t===== User Privilege Analysis ====={reset}
{green}[ ✓ ]{reset}{blue} User ID:{reset} {results["user_analysis"]['user_id']}
{green}\n[ ✓ ]{reset}{blue} Sudo Privileges:{reset}\n{results["user_analysis"]['sudo_privilege_test']}
{green}\n[ ✓ ]{reset}{blue} All Users:{reset}\n{results["user_analysis"]['all_users']}
{green}\n[ ✓ ]{reset}{blue} Root Users:{reset}\n{results["user_analysis"]['root_users']}

{green}\n\t===== System Information ====={reset}
{green}\n[ ✓ ]{reset}{blue} Kernel Info:{reset} {results["system_analysis"]['kernal_info']}
{green}\n[ ✓ ]{reset}{blue} Sudo Version:{reset} {results["system_analysis"]['sudo_version']}
{green}\n[ ✓ ]{reset}{blue} Capabilities:{reset}\n{results["system_analysis"]['capabilities_info']}
{green}\n[ ✓ ]{reset}{blue} Crontab Tasks:{reset}\n{results["system_analysis"]['crontabs_info']}

{green}\n\t===== File Privilege Analysis ====={reset}
{green}\n[ ✓ ]{reset}{blue} SUID Binaries:{reset}\n{results["file_analysis"]['suid_bins']}
{green}\n[ ✓ ]{reset}{blue} SGID Binaries:{reset}\n{results["file_analysis"]['sgid_bins']}
{green}\n[ ✓ ]{reset}{blue} Writable Env PATH:{reset}\n{results["file_analysis"]['writable_env_path']}
"""
        print(output)
        end_time=perf_counter()
        print(f"Time taken to complete : {end_time-start_time}")
        #print(self.file_analysis.get_writable_permission_dirs_in_env_path().stdout)
        
    
    def start(self):
        self.core_handler()
        
        
if __name__ == "__main__":
    core=RootEscCore()
    core.core_handler()
