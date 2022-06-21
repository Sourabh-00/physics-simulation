# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:34:41 2022

@author: sourabh
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,5,0.1)
y=np.arange(-5,5,0.1)
X,Y=np.meshgrid(x,y)
u=((X)/(((X)**2+(Y+3)**2)**1.5))+((X)/(((X)**2+(Y-3)**2)**1.5))+((X)/(((X)**2+(Y+2)**2)**1.5))+((X)/(((X)**2+(Y-2)**2)**1.5))+((X)/(((X)**2+(Y)**2)**1.5))+((X)/(((X)**2+(Y-1)**2)**1.5))+((X)/(((X)**2+(Y+1)**2)**1.5))
v=((Y+3)/(((X)**2+(Y+3)**2)**1.5))+((Y-3)/(((X)**2+(Y-3)**2)**1.5))+((Y+2)/(((X)**2+(Y+2)**2)**1.5))+((Y-2)/(((X)**2+(Y-2)**2)**1.5))+((Y)/(((X)**2+(Y)**2)**1.5))+((Y-1)/(((X)**2+(Y-1)**2)**1.5))+((Y+1)/(((X)**2+(Y+1)**2)**1.5))
plt.figure(figsize=(10, 10))
plt.streamplot(X,Y,u,v,density=3,linewidth=None,color='k')
plt.plot(0,-3,'og')
plt.plot(0,3,'or')
plt.plot(0,-2,'ob')
plt.plot(0,2,'oy')
plt.plot(0,0,'oc')
plt.plot(0,-1,'ok')
plt.plot(0,1,'om')
plt.grid()
plt.show()

