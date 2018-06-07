# _*_ coding: utf-8 _*_
# 程式 13-1 (Python 3 Version)

import matplotlib.pyplot as pt
x = [1, 2, 3, 4, 5, 6]
y = [1, 1, 1, 1, 1, 1]


pt.bar(x, y, label='Mary', color='red')
pt.xlabel('month')
pt.ylabel('dollars (million)')
pt.legend()
pt.title('Program 13-1')
pt.show()
