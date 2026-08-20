import numpy as np
# 1. Broadcasting with scalar
arr = np.array([10, 20, 30])
result = arr + 5
print("1. Scalar Broadcasting:")
print(result)

# 2. Broadcasting with 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
result = arr + 10
print("\n2. 2D Array Broadcasting:")
print(result)


# 3. Broadcasting two arrays
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
arr2 = np.array([10, 20, 30])
result = arr1 + arr2
print("\n3. Broadcasting Two Arrays:")
print(result)

# 4. Broadcasting with multiplication
prices = np.array([100, 200, 300])
result = prices * 1.10
print("\n4. Broadcasting with Multiplication:")
print(result)
# 5. Broadcasting with subtraction
marks = np.array([[80, 90, 70],
                 [60, 75, 85]])
result = marks - 5
print("\n5. Broadcasting with Subtraction:")
print(result)

# 6. Broadcasting with division
arr = np.array([100, 200, 300])
result = arr / 10
print("\n6. Broadcasting with Division:")
print(result)

# 7. Row/Column broadcasting
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

values = np.array([[10],
                   [20]])

result = arr + values
print("\n7. Row/Column Broadcasting:")
print(result)