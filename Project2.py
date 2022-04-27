#!/usr/bin/env python
# coding: utf-8

# In[27]:


from scipy.optimize import linprog
from fractions import Fraction

num1 = input(" Input number ") #first number
num2 = input(" Input number ") #second number
num1 = float(Fraction(num1)) #convert to float
num2 = float(Fraction(num2)) # convert to float if input is
if (num1*num2 == 1.0):
    print(" The multiplication of pairs gives " + str(num1*num2)) # if the product is 1.0
elif (num1*num2 < 0): 
     print(" Please enter positive integers ") # In case input is negative
elif(num1*num2 != 1): # if the product isn't 1, optimization follows
    a = num1*num2 
    obj = [a] #objective function to be minimized 
    left_eq = [[a],[a]] #left part of the equation
    right_eq = [[1],[1]] #right part of the equation
    bnd = [(0, float("inf"))]
    opt = linprog(c=obj, A_eq = left_eq, b_eq = right_eq, bounds = bnd, method = "revised simplex") #minimizing
    print(" Variable adjustment " + str(opt.x))
    print(opt)


# In[ ]:





# In[ ]:




