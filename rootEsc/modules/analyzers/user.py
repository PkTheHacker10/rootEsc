from subprocess import run

class UserAnalysis():
    def __init__(self):
        pass
    
    def get_all_users(self):
        all_users_output=run("cat /etc/passwd ",capture_output=True,shell=True)
        return all_users_output
    
    def get_current_user_id(self):
        user_id_output=run("id",capture_output=True,shell=True)
        return user_id_output
    
    def get_sudo_privileges(self):
        sudo_privilege_output=run("sudo -nl ",capture_output=True,shell=True)
        return sudo_privilege_output
    
    def get_user_permited_files(self):
        pass
