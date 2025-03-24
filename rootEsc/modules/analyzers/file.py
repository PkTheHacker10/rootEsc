from subprocess import run

class FileAnalysis():

    def get_suid_bins(self):
        suid_bins_output=run("find / -type f -perm -04000 2>/dev/null",capture_output=True,shell=True)
        return suid_bins_output
    
    def get_sgid_bins(self):
        sgid_bins_output=run("find / -type f -perm -02000 2>/dev/null",capture_output=True,shell=True)
        return sgid_bins_output
    
    def get_writable_permission_dirs_in_env_path(self):
        pass
    
    def get_readable_text_files(self):
        pass