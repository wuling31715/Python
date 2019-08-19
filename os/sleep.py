import os, getpass

def sleep():
    command = 'open -a ScreenSaverEngine'
    os.system(command)
    
def main():
    sleep()

if __name__ == "__main__":
    main()