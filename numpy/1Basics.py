#learning numpy basics
import numpy as np
# Create a 1D array
arr = np.array([1,2,3,4,5])
print("1D Array:", arr)
# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2d)
# Create a 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", arr3d)
#operations
print("Shape of arr:", arr.shape)  
print("Shape of arr2d:", arr2d.shape)
print("Shape of arr3d:", arr3d.shape)
#arithmetic operations
arr_sum = arr + 10
print("Array after adding 10:", arr_sum)
arr_product = arr * 2
print("Array after multiplying by 2:", arr_product)
arr_mean = np.mean(arr)
print("Mean of arr:", arr_mean)
arr_std = np.std(arr)
print("Standard deviation of arr:", arr_std)
# Indexing and slicing
print("First element of arr:", arr[0])
print("First row of arr2d:", arr2d[0])
#2d array arithmetic
arr2d_sum = arr2d + 10
print("2D Array after adding 10:\n", arr2d_sum)
arr2d_product = arr2d * 2
print("2D Array after multiplying by 2:\n", arr2d_product)
# Indexing and slicing in 2D array  

matrix = np.arange(1,13).reshape(3, 4)
print("First row of arr2d:", matrix)
#slicing matrix
sub_matrix= matrix[1:,1:3]
print("Sub-matrix (from 2nd row and 2nd to 3rd column):\n", sub_matrix)
# Inde