arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def test(arr):
    for i in arr:
        if i % 2 == 0:
            yield 0
        else:
            yield 1
result = list(test(arr))
print(result)
