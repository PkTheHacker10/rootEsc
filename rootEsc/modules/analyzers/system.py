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
    
