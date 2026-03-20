import numpy as  np

# Define random Arrays
np.random.seed(0)
array1 = np.random.randint(10, size=4)
print("arrary1: ", array1)

array2 = np.random.randint(10, size=(2, 4))
print("array2: ", array2)

array3 = np.random.randint(10, size=(3, 4, 5))
print("array3: ", array3)

print("numpy array attributes example:")
print("array3 ndim: ", array3.ndim)
print("array3 shape: ", array3.shape)
print("array3 size: ", array3.size)
print("array3 dtype: ", array3.dtype)
print("array3 itemsize: ", array3.itemsize, "bytes")
print("array3 nbytes: ", array3.nbytes, "bytes")