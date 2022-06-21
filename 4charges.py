# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:49:04 2022

@author: sourabh
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,5,0.1)
y=np.arange(-5,5,0.1)
X,Y=np.meshgrid(x,y)
u=((X+3)/(((X+3)**2+(Y+3)**2)**1.5))+((X+3)/(((X+3)**2+(Y-3)**2)**1.5))+((X-3)/(((X-3)**2+(Y+3)**2)**1.5))+((X-3)/(((X-3)**2+(Y-3)**2)**1.5))
v=((Y+3)/(((X+3)**2+(Y+3)**2)**1.5))+((Y-3)/(((X+3)**2+(Y-3)**2)**1.5))+((Y+3)/(((X-3)**2+(Y+3)**2)**1.5))+((Y-3)/(((X-3)**2+(Y-3)**2)**1.5))
plt.figure(figsize=(10, 10))
plt.streamplot(X,Y,u,v,density=3,linewidth=None,color='k')
plt.plot(-3,-3,'og')
plt.plot(-3,3,'or')
plt.plot(3,-3,'ob')
plt.plot(3,3,'oy')
plt.grid()
plt.show()
#i made this because i thought there's only 1 point in a square arrangment of positive equal ccharges but as i can see there's actually 5 points with zero electric field

