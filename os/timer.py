import os, time

def countdown(second):
    for i in range(second):
        print(second - i, end=' ', flush=True)
        time.sleep(1)
    print()

def main():
    second = int(input('second: '))
    countdown(second)
    command = 'open -a ScreenSaverEngine'
    os.system(command)

if __name__ == "__main__":
    main()