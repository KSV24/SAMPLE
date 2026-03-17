#import numpy_1 as np

#arr = np.array([1,2,3,4,5])
#print(arr)
#print(type(arr))

#string=" virat kohli "
#print(string.strip())
#for character in string:
#    print(character,end=",")


import numpy as np
data = np.array([[10, 20, 30],
                 [40, 50, 60]])
print("Array:\n", data)
print("Mean (row-wise):", np.mean(data, axis=1))
print("Mean (column-wise):", np.mean(data, axis=0))