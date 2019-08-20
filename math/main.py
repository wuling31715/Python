import math

def log(x, y):
    return math.log(x, y)

def factorial(x):
    return math.factorial(x)

def main():
    while True:
        try:
            function = input('function: ')
            parameter = function.split()
            if function == '':
                break
            elif 'l' in function:            
                x, y = float(parameter[-2]), float(parameter[-1])
                result = log(y, x)
            elif 'f' in function:
                x = int(parameter[-1])
                result = factorial(x)
            else:
                result = eval(function)
            print(' = %s' % result)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()