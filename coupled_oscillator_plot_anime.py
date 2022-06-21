# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 13:59:19 2022

@author: sourabh
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as odeint
import matplotlib.animation as animation
fig, ax = plt.subplots()
def f(u,t):
    #massses and spring constants
    #spring constant of 1st and 3rd spring is taken same in differential equations
    k1=4
    k2=0.5
    m1=0.1
    m2=0.1
    #differential equations
    dX1=u[1]
    d2X1=-(k1/m1)*u[0]-(k2/m1)*(u[0]-u[2])
    dX2=u[3]
    d2X2=-(k1/m2)*u[2]-(k2/m2)*(u[2]-u[0])
    return [dX1,d2X1,dX2,d2X2]
t=np.linspace(0,30,1000)
#initial condition [displacement,velocity,displacement,velocity]
#initial veocity doesn't make a difference
y0=[1,0,0,0]
sol=odeint(f,y0,t)
x1=sol[:,0]
x2=sol[:,2]
plt.ylim(-2,2)
ax.plot(t,x1)
ax.plot(t,x2)
plt.xticks(np.arange(min(t),max(t)+1,2))
plt.xlabel('time(s)')
plt.ylabel('displacement')
plt.legend(['1st mass','2nd mass'],loc='upper right')
#two dots to be animated now putting them at their initial position comma is neccessary while defining this for some reason
bluedot,=plt.plot([0],x1[0],'bo')
reddot,=plt.plot([0],x2[0],'ro')
#defining a function which updates the positions of those dots
def animate(i):
    reddot.set_data(t[i],x2[i])
    bluedot.set_data(t[i],x1[i])
    return reddot,bluedot
#interval of 30 milisec don't work for some reason to complete 30 sec definde in t matrix
#20 millisec interval also takes around 35 sec to complete cycle of 30 sec
#but 10 millisec takes 11 sec to complete cycle of 30 sec idk why?
#magic happpens here
myanime=animation.FuncAnimation(fig,animate,frames=len(t),interval=30,blit=True,repeat=True)
plt.show()    
