import numpy as np 
arr1 = np.array ([[1,2,3],[4,5,6]])
print("Matrix 1 :",arr1)
arr2 = np.array([[7,8,9], [10,11,12]])
print("Matrix 2 :",arr2)

arr3 = arr1 + arr2
print("Addition :",arr3)

arr3 = arr2 - arr1 
print("Subtraction:", arr3)

arr3 = arr2 @ arr1.T
print ("Multiplication:", arr3)

arr3 = arr2 / arr1
print("Division:", arr3)


arr3 = arr2 // arr1
print("Floor Division:" , arr3)