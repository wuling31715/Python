def layer1():
    a = 0
    def layer2():
        b = 1
        print(a)
    layer2()
    try:
        print(b)
    except:
        print('error')

layer1()

