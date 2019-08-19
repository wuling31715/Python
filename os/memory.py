import os, time, getpass

def count_down(second):
    for i in range(second):
        print(second - i, end=' ', flush=True)
        time.sleep(1)
    print()

def sudo_purge(password):
    command = 'purge'
    os.system('echo %s|sudo -S %s' % (password, command))

def main():
    password = getpass.getpass('password: ')
    counter = 0
    while True:
        sudo_purge(password)
        counter += 1
        print('sudo purge: %d' % counter)
        count_down(300)

if __name__ == "__main__":
    main()