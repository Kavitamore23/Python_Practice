#!/usr/bin/env python
# coding: utf-8

# Use for, split() and if to create a statement that will print out words that start with 's'

# In[18]:


st = 'Welcome to our size youtube Same as channel kavish '


# In[19]:


st.split()


# In[20]:


for word in st.split():
    if word[0] == 's' or word[0]=='S':
        print (word)


# Use range() to print all the even numbers form 0 to 10

# In[21]:


list(range(0,11,2))


# In[25]:


for num in range(0,11, 2):
    print(num)
    


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divesible by 3

# In[33]:


[num for num in range (1,51)if num%3 == 0]


# Go through the string below and if the length of a word is even print"even!"

# In[43]:


st = "Hello, How are y"
for word in st.split():
    if len(word) %2 ==0:
        print(word + ' is Even')


# Write a program that prints the integers from 1 to 100. but for multiplies of three print "fizz" instrad of the numer, abd for the multiplies of five print "buzz" for number which are multiplies of both three and five print "Fizzbuzz"

# In[45]:


for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0 :
        print('Fizzbuzz')
    elif num %3 == 0:
        print("Fizz")
    elif num %5 == 0 :
        print("Buzz")
    else :
        print(num)


# Use list comprehension to create a list of the first letters of every word in thestring below:

# In[46]:


st= "Heloo Word its very you can do it"
[word[0] for word in st.split()]


# In[ ]:




