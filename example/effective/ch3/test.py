arr = []
for i in range(1,101):
    arr.append(i)

it = (len(arr) for i in arr if i % 2 == 0)

print(next(it))
print(next(it))
