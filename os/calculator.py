import math

def numerical(function):
    function_list = function.split()
    for i, j in enumerate(function_list):
        if 'pi' == j:
            function_list[i] = str(math.pi)
        elif 'pi' in j:
            function_list[i] = j[:-2] + '*' + str(math.pi)
        if 'e' == j:
            function_list[i] = str(math.e)
        elif 'e' in j:
            function_list[i] = j[:-1] + '*' + str(math.e)
        if '!' in j:
            function_list[i] = str(math.factorial(int(j[:-1])))
    for i, j in enumerate(function_list):
        if 'l' in j:
            function_list[i] = str(math.log(float(function_list[i+2]), float(function_list[i+1])))
            function_list[i+1], function_list[i+2] = '', ''
    function = str()
    for i in function_list:
        function = function + i + ' '
    return function

def main():
    while True:
        try:
            function = input('function: ')
            function = numerical(function)
            if function == '':
                break
            else:
                result = eval(function)
            print(' = %s' % result)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()