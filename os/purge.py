import os, time, getpass
from timer import countdown

def purge(password):
    command = 'purge'
    os.system('echo %s|sudo -S %s' % (password, command))

def main():
    password = getpass.getpass('password: ')
    counter = 0
    while True:
        purge(password)
        counter += 1
        print('sudo purge: %d' % counter)
        countdown(300)

if __name__ == "__main__":
    main()