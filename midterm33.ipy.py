#!/usr/bin/env python
# coding: utf-8

# # develop a recursive function tough() that takes two nonnegative integer arguments and outputs a pattern

# In[1]:


def tough (indent, num) :
     if(num > 0):
        tough (indent, num//2)           # print previous pattern
        print(" "*indent + "*"*num)        # print middle row of *'s
        tough (indent + 1, num//2)        # print previous pattern indented
        
#function call
print("\n f(0,0) \n")
tough(0,0)
print("\n f(0,1) \n")
tough(0,1)
print("\n f(0,2)  \n")
tough (0,2)
print("\n f(0,4) \n")
tough(0,4)


# In[ ]:




