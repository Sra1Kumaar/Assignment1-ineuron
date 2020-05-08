#!/usr/bin/env python
# coding: utf-8

# # Task 1

# In[ ]:


# 1.Install Jupyter notebook and run the first program and share the screenshot of the output.


# In[4]:


a="My First Program In Jupyter Notebook"
print(a)


# In[ ]:





# In[ ]:


# 2.Write a program which will find all such numbers which are divisible by 7 but are not a multiple
    of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
    comma-separated sequence on a single line.


# In[17]:


n=range(2000,3201)
m=[]
for i in n:
    if (i%7==0)and(i%5!=0):
        m.append(i)


# In[18]:


m


# In[20]:


n=range(2000,3201)
m=[]
for i in n:
    if (i%7==0)and(i%5!=0):
        m.append(str(i))
print(','.join(m))


# In[ ]:





# In[ ]:


# 3.Write a Python program to accept the user's first and last name and then getting them printed in
    the the reverse order with a space between first name and last name.


# In[26]:


a=input("first name:")
b=input("last name:")
print(b,a)


# In[ ]:





# In[ ]:


# 4.Write a Python program to find the volume of a sphere with diameter 12 cm.
    Formula: V=4/3 * π * r 3


# In[29]:


π=3.14159
r=6
v=4/3*π*r**3
print("volume of the sphere:",v)


# In[ ]:





# # Task 2

# In[ ]:





# In[ ]:


# 1.Write a program which accepts a sequence of comma-separated numbers from console and
    generate a list.


# In[40]:


n=input("comma-seperated numbers:")
list=n.split(',')
print("list:",list)


# In[ ]:





# In[ ]:


# 2.Create the below pattern using nested for loop in Python.
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *


# In[41]:


for i in range(0,6):
    for j in range(i):
        print('*',end="")
    print('')
for i in range(6,0,-1):
    for j in range(i):
        print('*',end="")
    print('')


# In[ ]:





# In[ ]:


# 3.Write a Python program to reverse a word after accepting the input from the user.


# In[1]:


a=input("word to be reversed:")

for char in range(len(a)-1,-1,-1):
    print(a[char],end="")
print("\n")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




