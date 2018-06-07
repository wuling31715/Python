a = 1
b = 'b'

print(' a = %s, b = %s' % (a,  b))

x = [i for i in range(1, 101)]
for i in x:
    print(x[i - 1])


def args(x, *y):
    z = x + y
    return z


 print(args(1, 1))
 print(args(1, 0))

