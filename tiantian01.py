#%%[markdown]
'''
Author: your name
Date: 2021-09-08 20:39:56
LastEditTime: 2021-09-12 10:59:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \0001\tiantian01.py
'''
#%%
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(0, 20, 100)
plt.plot(x,np.sin(x))
#%%
a = 1
b = 1
c = 1
for a in range(100) :
  for b in range(100):
     for c in range(100):        
        if b!=a and  b!=c:
           d1=a*b*c 
           d2=a+b+c 
           if d1==d2 :
              print('a*b*c=a+b+c', 'a=', a, 'b=', b, 'c=', c)


# %%



