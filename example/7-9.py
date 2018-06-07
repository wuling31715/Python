def pick(x):
    fruits = ['Apple', 'Banana', 'Orange', 'Tomato', 'Pine Apple', 'Berry']
    return fruits[x]

alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]
choices = map(pick, alist)
for choice in choices:
    print(choice)
