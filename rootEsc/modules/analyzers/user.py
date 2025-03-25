from subprocess import run

class UserAnalysis():
    def __init__(self):
        pass
    
    def get_all_root_users(self):
        all_root_users_output=run("awk -F: '($3 == \"0\") {print}' /etc/passwd",capture_output=True,shell=True)
        return all_root_users_output
    
    def get_all_users(self):
        all_users_output=run(f"cat /etc/passwd | cut -d \":\" -f 1",capture_output=True,shell=True)
        return all_users_output
    
    def get_current_user_id(self):
        user_id_output=run("id",capture_output=True,shell=True)
        return user_id_output
    
    def get_sudo_privileges(self):
        sudo_privilege_output=run("sudo -nl",capture_output=True,shell=True)
        return sudo_privilege_output
    
