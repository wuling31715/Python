import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random


data1 = pd.read_csv('class/data/001.csv')
data2 = pd.read_csv('class/data/002.csv')
data3 = pd.read_csv('class/data/003.csv')

arr_data1 = data1.as_matrix()
arr_data2 = data2.as_matrix()
arr_data3 = data3.as_matrix()


#print(len(arr_np1))
#print(len(arr_np2[:100]))

arr_merge = np.concatenate((arr_data1,arr_data2[:100], arr_data3[:100]), axis=1)
arr_sorted = sorted(arr_merge, key = lambda arr_merge: arr_merge[2])


for row in arr_sorted:
    print(row)
