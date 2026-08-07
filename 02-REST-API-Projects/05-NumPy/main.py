import numpy as np

a = np.array([1,2,3,4,5,6])
print(a)
print( a * 2)

#-------------------------
b = [1,2,3,4,5,6]
print(b * 2 )

## 2 Dimentional Array
arr2 = np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
    ])

## 3 Dimentional Array
arr3 = np.array([
    [[1,2,3],
    [4,5,6]],

    [[7,8,9],
    [10,11,12]],

    [[21,22,23],
    [24,25,26]]

])

print(a.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(a.shape)
print(arr2.shape)
print(arr3.shape)

arr4 = np.array([10, 20, 30, 40, 50], dtype=float)
print(arr4)
print(arr4[-1])

print(arr4[0:4])  #Slicing to get sub intergers

arr = np.zeros((3,2,3))
print(arr)


arr=np.arange(1, 11, 2)
print(arr)

#----------------------------------------------------------------


