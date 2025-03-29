from modules.core import RootEscCore
from modules.cli.cli import CommandLine
from colorama import Fore,Style

red=Fore.RED
green=Fore.GREEN
reset=Style.RESET_ALL

class RootEsc():
    # Class to manage the rootESC tool. 
    def __init__(self):
        self.cli=CommandLine()

    def core(self):
        # Core funtion that starts the rootESC.

        # Checking for no banner flag.
        if not self.cli.args().no_logging:
            print(f"""{red}
    ░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░▒▓████████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  
                                                                                            
    {reset}  
                                                                        Author  : {green}Pevinkumar A {reset}
                                                                        Version : {green}v1.1 {reset}                                                                                   
""")

        root_esc_core=RootEscCore()
        root_esc_core.start()
        
def main():
    # Main function to core .
    rootesc=RootEsc()
    rootesc.core()

if __name__ == "__main__":
    main()