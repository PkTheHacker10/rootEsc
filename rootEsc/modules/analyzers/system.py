from subprocess import run

class SystemAnalysis():
    
    def get_kernel_info(self):
        kernal_info_output=run(["uname","-a"],capture_output=True,text=True)
        return kernal_info_output
    
    def get_sudo_version(self):
        sudo_info_output=run(["sudo","-V"],capture_output=True,text=True)
        return sudo_info_output
    
    def get_crontabs_tasks(self):
        crontabs_info_output=run(["cat /etc/crontab | grep -v '^#'"],capture_output=True,text=True,shell=True)
        return crontabs_info_output
    
    def get_capabilities(self):
        capabilities_info_output=run(["getcap","-r","/"],capture_output=True,text=True)
        return capabilities_info_output
    
    def get_all_root_users(self):
        all_root_users_output=run("awk -F: '($3 == \"0\") {print}' /etc/passwd",capture_output=True,shell=True,text=True)
        return all_root_users_output
    
    def get_all_users(self):
        all_users_output=run(f"cat /etc/passwd | cut -d \":\" -f 1",capture_output=True,shell=True,text=True)
        return all_users_output
    
    def get_current_user_id(self):
        user_id_output=run("id",capture_output=True,shell=True,text=True)
        return user_id_output
    
    def get_sudo_privileges(self):
        sudo_privilege_output=run("sudo -nl",capture_output=True,shell=True,text=True)
        return sudo_privilege_output
