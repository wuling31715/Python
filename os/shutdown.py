import os, getpass

def shutdown(password):
    command = 'shutdown -h now'
    os.system('echo %s|sudo -S %s' % (password, command))
    print('shutdown...')

def main():
    password = getpass.getpass('password: ')
    shutdown(password)

if __name__ == "__main__":
    pass