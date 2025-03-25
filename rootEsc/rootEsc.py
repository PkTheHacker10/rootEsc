from modules.core import RootEscCore

class RootEsc():
    def core(self):
        root_esc_core=RootEscCore()
        root_esc_core.start()
        
def main():
    rootesc=RootEsc()
    rootesc.core()

if __name__ == "__main__":
    main()