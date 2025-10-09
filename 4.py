import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

add_arr = arr + 5

print("Array after adding 5:", add_arr)

mul_arr = arr * 2

print("Array after multiplying by 2:", mul_arr)

total = np.sum(arr)

print("Sum of array elements:", total)

mean_val = np.mean(arr)

print("Mean of array elements:", mean_val)

print("Maximum value:", np.max(arr))

print("Minimum value:", np.min(arr))

sorted_arr = np.sort(arr)

print("Sorted Array:", sorted_arr)

sqrt_arr = np.sqrt(arr)

print("Square Root of each element:", sqrt_arr)
