import numpy as np

data = np.array(np.random.randint(1, 100, size=25)).reshape(5, 5)

# Matrix manipulation - Swap the second and fourth rows of the data matrix.

print(data)
data[[1, 3]] = data[[3, 1]]
print(data)

# Normalization - Normalize all the elements in the data matrix such that they are scaled to range between 0 and 1.
# Hint: to normalize, subtract the minimum and divide by the max-min.


def normalize(data_matrix):
    min_values = np.min(data_matrix, axis=0)
    max_values = np.max(data_matrix, axis=0)
    range_values = max_values - min_values

    # Avoid division by zero
    range_values[range_values == 0] = 1

    normalized_data = (data_matrix - min_values) / range_values
    return normalized_data


normalized_data = normalize(data)

print(normalized_data)

# Z-score normalization - Standardize the data matrix using Z-score normalization.
# That is, all the elements should be scaled to have a mean* of 0 and a standard deviation of 1.
# Z-score is calculated as (X - mean) / std.


def zscore_normalization(data_matrix):
    mean = np.mean(data_matrix, axis=0)
    std = np.std(data_matrix, axis=0)

    # Avoid division by zero
    std[std == 0] = 1

    normalized_data = (data_matrix - mean) / std
    return normalized_data


z_normalized_data = zscore_normalization(data)

print(z_normalized_data)

# Array splitting - Reshape the data matrix into a vector
# (Hint: use np.ravel) and split this array into five equal-sized sub-arrays.

vector = np.ravel(data)

arrays = np.array_split(vector, 5)

print(arrays)


# Dot product - Create two vectors of size 5 with any values. Compute the dot product of the two vectors*.

vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

dot_product = np.dot(vector1, vector2)

print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Dot Product:", dot_product)

# Matrix multiplication - Create another 3x3 matrix with any values (let’s call it data2).
# Perform matrix multiplication (dot product of data (first 3x3 part) and data2).

data2 = np.array(np.random.randint(1, 100, size=9)).reshape(3, 3)

data_subset = data[:3, :3]

result = np.dot(data_subset, data2)

print("Matrix data (3x3 subset):\n", data_subset)
print("\nMatrix data2:\n", data2)
print("\nMatrix Multiplication Result:\n", result)

# Inverse of a matrix - Create a 3x3 identity matrix*, multiply it with 2 and compute its inverse.

identity_matrix = np.eye(3)
print(identity_matrix)

multiplied_matrix = identity_matrix * 2
print(multiplied_matrix)

inverse_matrix = np.linalg.inv(multiplied_matrix)
print(inverse_matrix)


# Eigenvalues and eigenvectors - For the first 3x3 part of the data matrix, compute the eigenvalues and eigenvectors*.

eigenvalues, eigenvectors = np.linalg.eig(data_subset)
print(eigenvalues)
print(eigenvectors)

# Find missing values - Replace random 5 elements in the data matrix with np.nan. Find the indices of the missing values.
print(data)
float_data = data.astype(float)

rand_rows = np.random.choice(float_data.shape[0], 5)
rand_cols = np.random.choice(float_data.shape[1], 5)
float_data[rand_rows, rand_cols] = np.nan
print("Modified Data:\n", float_data)

missing_indices = np.where(np.isnan(float_data))
print(missing_indices)

# Replace missing values - Replace the missing values in the data matrix
# with the mean of the matrix (ignoring the missing values while computing the mean).

float_data[np.isnan(float_data)] = np.nanmean(float_data)
print(float_data)