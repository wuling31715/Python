import itertools

x = [i for i in range(1, 10)]
# print(list(itertools.permutations(x)))

def main(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    if (10 * x1 + x2) * x3 == 10 * x4 + x5 and 10 * x4 + x5 + 10 * x6 + x7 == 10 * x8 + x9:
        return True

for i in list(itertools.permutations(x)):
    x1, x2, x3, x4, x5, x6, x7, x8, x9 = i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]
    if main(x1, x2, x3, x4, x5, x6, x7, x8, x9):
        print(i)
        break