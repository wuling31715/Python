import os, getpass

def lock():
    command = 'open -a ScreenSaverEngine'
    os.system(command)
    
def main():
    lock()

if __name__ == "__main__":
    main()