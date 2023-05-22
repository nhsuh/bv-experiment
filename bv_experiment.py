#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import math
import matplotlib.pyplot as plt


# Large sample of $(x_1, x_2)$, derive average $a$ and $b$ from sample. These $a$ and $b$ will be used in $g(x)$ and $E_{out}$

# In[31]:


x_1 = np.random.uniform(-1, 1, 10000)
x_2 = np.random.uniform(-1, 1, 10000)
a_avg_g = np.mean(x_2 + x_1)
b_avg_g = np.mean(np.multiply(-x_1, x_2)**2)
a2_avg_g = np.mean((x_2 + x_1) **2)
b2_avg_g = np.mean(np.multiply(-x_1, x_2)**2)


# In[32]:


#g(x) = (a_avg_g)(x) + b_avg_g
e_out = b2_avg_g + (a2_avg_g)/3 + (1/5) - 2*b_avg_g/3
print("avg g(x) = ", a_avg_g, "x + ", b_avg_g )
print("E_out: ", e_out)


# $h(x)$ function, evaluates based on $a$, $b$, and inputted $x$

# In[33]:


def h(a, b, x):
    return a * x + b;


# Calculate bias by taking the average of the mean squared difference between $g(x)$ and $f(x)$

# In[34]:


x_list = np.random.uniform(-1, 1, 1000)
bias = np.mean(np.square(h(a_avg_g, b_avg_g, x_list) - np.square(x_list)))
print("Bias: ", bias)


# Calculate variance by taking the average with respect to x of the average with respect to D of the mean squared difference between h(x) and g(x)

# In[35]:


var_outer_list = np.array([])
for x in x_list:
    var_inner_list = np.array([])
    x_1 = np.random.uniform(-1, 1, 100)
    x_2 = np.random.uniform(-1, 1, 100)
    for i in range(len(x_1)):
        a_h = x_1[i] + x_2[i]
        b_h = -x_1[i] * x_2[i]
        var_inner_list = np.append(var_inner_list, [np.square(h(a_h, b_h, x) - h(a_avg_g, b_avg_g, x))])
    var_outer_list = np.append(var_outer_list, [np.mean(var_inner_list)])
var = np.mean(var_outer_list)
print("Variance: ", var)
        


# Graph g(x) and f(x)

# In[36]:


x_graph = np.linspace(-1, 1, 100)
plt.plot(x_graph, x_graph**2, label="f(x)")
plt.plot(x_graph, h(a_avg_g, b_avg_g, x_graph), label ="avg g(x)")
plt.xlabel("x")
plt.ylabel("f(x) or avg g(x)")
plt.title("Target Function and Average Function")
plt.legend()
plt.show()

