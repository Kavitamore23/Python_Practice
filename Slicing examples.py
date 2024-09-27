#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

#2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

#3. Write a NumPy program to create an array with values ranging from 12 to 38.

#4. Write a NumPy program to convert a list and tuple into arrays. Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8] 

#Input: my_tuple = ([8, 4, 6], [1, 2, 3])


# In[2]:


#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives
import numpy as np

zeros_array = np.zeros(10)
ones_array = np.ones(10)
fives_array = np.full(10, 5)

print("Array of 10 zeros:", zeros_array)
print("Array of 10 ones:", ones_array)
print("Array of 10 fives:", fives_array)



# In[3]:


#2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
import numpy as np

# Create an array with values from 2 to 10
array = np.arange(2, 11)

# Use slicing to create a 3x3 matrix
matrix = array[:9].reshape(3, 3)

print(matrix)


# In[7]:


#3. Write a NumPy program to create an array with values ranging from 12 to 38.

import numpy as np

# Create an array with values ranging from 12 to 38
array = np.arange(12, 39)

print(array)


# In[11]:


#4. Write a NumPy program to convert a list and tuple into arrays. Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8] 
import numpy as np 
my_list = [1,2,3,4,5,6,7,8]
my_tuple=([8, 4, 6], [1, 2, 3])

array1= np.array(my_list)[:]
array2 = np.array(my_tuple)[:]

print("List into array using slicing",array1)
print("List into tuple using slicing", array2)


# In[ ]:




