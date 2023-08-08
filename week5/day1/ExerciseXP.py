# Import the numpy package under the name np.
import numpy as np

# Create a vector* of zeros with size 10 using np.zeros().
zeros_array = np.zeros(10)
print(zeros_array)

# Compute the memory size* of any array. Note: You can do this by multiplying the length of
# the array by the size of one array element, which you can find using the .itemsize attribute.
print(zeros_array.itemsize * zeros_array.size)

# Retrieve the documentation of the numpy add function from the command line.
# print(np.info(np. add))

# Create a vector with values ranging from 10 to 49 using np.arange().
new_array = np.arange(10, 50)
print(new_array)

# Reverse a vector so the first element becomes last (Hint: Use slicing).
print(new_array[::-1])

# Create a 3x3 matrix* with values ranging from 0 to 8 using np.reshape().
matrix = np.arange(0,9).reshape((3,3))
print(matrix)

# Find indices of non-zero elements from [1,2,0,0,4,0] using np.nonzero().
array = np.array([1, 2, 0, 0, 4, 0])
print(np.nonzero(array))

# Create a 3x3 identity matrix* using np.eye().
eye_matrix = np.eye(3)
print(eye_matrix)

# Create a 5x5 matrix with row values ranging from 0 to 4. The output should be a matrix where each row is [0, 1, 2, 3, 4].
row = np.arange(0, 5, dtype='float64' )
five_matrix = np.tile(row, (5, 1))
print(five_matrix)

# Create a vector of size 10 with values ranging from 0 to 1, both excluded. You can use np.linspace.
vector = np.linspace(0., 1., num=11, endpoint=False)[1:]
print(vector)

# Create a random vector of size 10 and sort it.
random_vector = np.sort(np.random.rand(10))
print(random_vector)

# Print the minimum and maximum representable value for each numpy scalar type*
# (int8, int32, int64, float32, float64). Use np.iinfo and np.finfo.
for item in ['int8', 'int32', 'int64']:
    print(np.iinfo(item).min ,np.iinfo(item).max)
for item in ['float32', 'float64']:
    print(np.finfo(item).min ,np.finfo(item).max)

# How to convert a float (32 bits) array into an integer (32 bits) in place? Use np.ndarray.astype.
float_array = np.arange(1,5, dtype='float32')
print(float_array)
int_array = float_array.astype(int)
print(int_array)

# Subtract the mean* of each row of a matrix. Use np.mean with axis=1.
random_matrix = np.random.randint([1, 3, 5, 7], [[30], [30], [30]])
float_matrix = random_matrix.astype(float)
row_mean = np.mean(random_matrix, axis=1).reshape(-1, 1)
print(float_matrix)
print(row_mean)
float_matrix -= row_mean
print(float_matrix)

# How to sort an array by the nth column? Use np.argsort.
n = -1
sorted_indices = np.argsort(float_matrix[:, n])
sorted_array = float_matrix[sorted_indices]
print(sorted_array)

# How to swap two rows of an array? You can do this using array indexing.
matrix1 = np.array([[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]])
matrix1[[0, 1]] = matrix1[[1, 0]]

print(matrix1)

# Given an array C that is a bincount*, how to produce an array A such that np.bincount(A) == C? Use np.repeat.
C = np.array([2, 3, 0, 1, 0, 2])

A = np.repeat(np.arange(len(C)), C)

print(A)

