#!/usr/bin/env python
# coding: utf-8

# Q)How do you create a NumPy array?		
# ==>To create numpy array we can use the numpy.array() function from numpy library

# In[1]:


import numpy as np
arr= np.array([1,2,3,4,5])
print(arr)


# Q2)How do you create a 2D array (matrix) in NumPy?		
# ==>To create a 2D array, you need to pass a list of lists (where each inner list represents a row) to the numpy.array()

# In[2]:


matrix = np.array([[1,2,3,4],[3,4,5,6]])
print(matrix)


# 
# Q3)How do you find the shape of an array?		
# ==>To find the shape of a NumPy array, you can use the .shape attribute.

# In[4]:


import numpy as np

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3,4], [4, 5, 6,3]])

# Find the shape of the array
shape = matrix.shape

print("Shape of the array:", shape)



# Q4)How do you get the data type of a NumPy array?		
# ==>To get the data type of a NumPy array, you can use the .dtype attribute
# 

# In[5]:


import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4])

# Get the data type of the array
data_type = array.dtype

print("Data type of the array:", data_type)


# Q5) How do you slice a NumPy array?		
# array[start:stop:step]
# 
# 

# In[7]:


import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6])

# Slice from index 1 to 4
sliced_array = array_1d[1:4]

print(sliced_array)


# In[9]:


# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

# Slice rows and columns (row indices 0 to 1, column indices 1 to 2)
sliced_matrix = matrix[0:2, 1:3]

print(sliced_matrix)


# Q6) How do you add or subtract two NumPy arrays?		
# ==>You can add or subtract two NumPy arrays using the + and - operators, respectively.

# In[12]:


import numpy as np
# Create two NumPy arrays
array_a = np.array([1, 2, 3])
array_b = np.array([4, 9, 9])
# Add the two arrays
sum_array = array_a + array_b
print("Sum of arrays:", sum_array)
# Subtract the two arrays
difference_array = array_a - array_b
print("Difference of arrays:", difference_array)


# Q7) How do you transpose a 2D NumPy array?		
# ==>Transposing a 2D NumPy array can be done using the .T attribute or the numpy.transpose() function.

# In[13]:


import numpy as np

# Create a 2D NumPy array (matrix)
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])

# Transpose the array
transposed_matrix = matrix.T

print("Original matrix:")
print(matrix)

print("\nTransposed matrix:")
print(transposed_matrix)


# Q8)How do you flatten a NumPy array?		
# 
# ==>Flattening a NumPy array refers to converting a multi-dimensional array into a one-dimensional array.
# The .flatten() method returns a copy of the array collapsed into one dimension.
# 
# 

# In[14]:


import numpy as np

# Create a 2D NumPy array (matrix)
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])

# Flatten the array
flattened_array = matrix.flatten()

print("Original matrix:")
print(matrix)

print("\nFlattened array:")
print(flattened_array)


# Q9) How do you perform element-wise multiplication in NumPy?
# ==>You can perform element-wise multiplication in NumPy using the * operator. This operator multiplies corresponding elements in two arrays of the same shape. If the arrays have different shapes, NumPy uses broadcasting to allow the operation.
# 
# 

# In[15]:


# Create a 1D array and a 2D array
array_1d = np.array([1, 2, 3])
array_2d = np.array([[4, 5, 6], 
                     [7, 8, 9]])

# Perform element-wise multiplication with broadcasting
result_broadcast = array_1d * array_2d

print("Result with broadcasting:\n", result_broadcast)


# Q10)How do you calculate the sum of elements in a NumPy array?		
# ==>You can calculate the sum of elements in a NumPy array using the numpy.sum() function or the .sum() method available on the array object

# In[22]:


import numpy as np
array= np.array([1,4,3,5,6,7,8])
total_sum=np.sum(array)
print("total_sum:", total_sum)


# Q11) How do you create an array of evenly spaced values?		
# ==>The numpy.linspace() function returns an array of evenly spaced values over a specified range. You can specify the start and end values, as well as the number of values you want.
# start: The starting value of the sequence.
# stop: The end value of the sequence.
# num: Number of samples to generate (default is 50).
# endpoint: If True, stop is the last sample. Otherwise, it is not included (default is True).
# retstep: If True, return (samples, step), where step is the spacing between samples.

# In[30]:


import numpy as np
array_linspace = np.linspace(1,10,num=5)
print("Array using linspace:",array_linspace)


# Q12)How do you create an array filled with zeros or ones?		
# ==>In NumPy, you can create arrays filled with zeros or ones using the numpy.zeros() and numpy.ones() functions

# In[33]:


import numpy as np
zeros_array = np.zeros((2,3))
print("Array filled with zero:")
print(zeros_array)


# In[35]:


import numpy as np
ones_array = np.ones((2,3))
print("Array filled with one:")
print(ones_array)


# Q13)Give a demonstartions of statistical operation on array		
# it includes calculating the mean, median, variance, standard deviation, and summation of elements in a NumPy array.
# 
# 

# In[42]:


import numpy as np
data = np.array([8,7,6,5,4])
#mean: The mean is the average of the array elements.
mean_value= np.mean(data)
print("mean",mean_value)
#median: The median is the middle value in a sorted array.
median_value= np.median(data)
print("median",median_value)
#variance: Variance measures how far each number in the set is from the mean.
variance_value = np.var(data)
print("variance:",variance_value)
#Standard_deviation : The standard deviation is the square root of the variance, representing the spread of the data.
std_deviation_value = np.std(data)
print("Standard Deviation:", std_deviation_value)
#sum : You can calculate the total sum of the elements in the array.
sum_value = np.sum(data)
print("Sum:", sum_value)




# Q14)Why do we need statistical functions 		
# WAP  for variance, std deviation

# In[43]:


import numpy as np

def calculate_variance(data):
    # Calculate the mean of the data
    mean = np.mean(data)
    
    # Calculate variance using the formula
    variance = np.sum((data - mean) ** 2) / len(data)
    
    return variance

def calculate_standard_deviation(data):
    # Calculate variance
    variance = calculate_variance(data)
    
    # Standard deviation is the square root of variance
    std_deviation = np.sqrt(variance)
    
    return std_deviation

# Example data
data = np.array([10, 20, 30, 40, 50])

# Calculate variance and standard deviation
variance = calculate_variance(data)
std_deviation = calculate_standard_deviation(data)

print("Variance:", variance)
print("Standard Deviation:", std_deviation)


# In[ ]:




