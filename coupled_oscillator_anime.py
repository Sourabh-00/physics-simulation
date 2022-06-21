# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 13:59:19 2022

@author: sourabh
"""
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams['animation.ffmpeg_path'] = r'C:\\ffmpeg-n5.0-latest-win64-lgpl-5.0\\bin\\ffmpeg.exe'
from scipy.integrate import odeint as odeint
import matplotlib.animation as animation
import time
fig, ax = plt.subplots()
def f(u,t):
    #massses and spring constants
    #spring constant of 1st and 3rd spring is taken same in differential equations
    k1=4
    k2=2
    m1=0.1
    m2=0.1
    #differential equations
    dX1=u[1]
    d2X1=-(k1/m1)*u[0]-(k2/m1)*(u[0]-u[2])
    dX2=u[3]
    d2X2=-(k1/m2)*u[2]-(k2/m2)*(u[2]-u[0])
    return [dX1,d2X1,dX2,d2X2]
t=np.linspace(0,100,10000)
#don't choose displacment greater than 4 because the spring length i have used is 4. if you do choose displacement greater than 4 springs willl be all over the place.
m1_disp=2
m2_disp=1
#initial condition [displacement,velocity,displacement,velocity]
#intial velocity won't make any difference
y0=[m1_disp,0,m2_disp,0]
sol=odeint(f,y0,t)
x1=sol[:,0]
x2=sol[:,2]
plt.ylim(-2,2)
plt.xlim(-9,9)
#ax.plot(t,x1)
#ax.plot(t,x2)
plt.xticks(np.arange(-9,9,1))
plt.xlabel('displacement')
#plt.ylabel('displacement')
#plt.legend(['1st mass','2nd mass'],loc='upper right')
#initial positions with -2,2 being position of masses when none of the spring is streched or squished
#walls are at 5.8 and -5.8 so that spring actually touches teh wall
plt.plot([-5.8,-5.8],[0.5,-0.5],'k',linewidth=5)
plt.plot([5.8,5.8],[0.5,-0.5],'k',linewidth=5)
#i will try to explain what i am doing below
#i need springs. 3 springs to be precise. i can get that with triangular wave
#i have shifted the triamgular wave 0.5 down and the period of triangular wave is given by the distance between two masses or one mass and wall divided by number like 4.5 or 3.5 etc. 
#i chose 4.5 and not 4 because i need some complete waves and a half wave so that the spring always ends at the mass otherwise spring will end after completeing the last triangle.
#than i plotted that wave and then animated it using animate function.
#if you see some random values i am adding or subrtacting from variables below that is due to trial and error to get the springs right.
m1_initial=-2+m1_disp
m2_initial=2+m2_disp
p=(m2_initial-m1_initial)/4.5
p1=(m1_initial+6)/4.5
p2=(6-m2_initial)/4.5
#p1/4 below added and subtracted is to end the shifted wave at x=0 otherwise it will end after completeing the triangle.
x11=np.arange(-6+(p1/4),m1_initial-(p1/4),0.01)
x22=np.arange(m2_initial+(p2/4),6-(p2/4),0.01)
#some values added to x coordinated below in tang function is so that wave ends at mass and wall
#0.5 subtracted from triangular wave equation to shift the trainagular wave down by 0.5and 0.5 factor multiplied is make the maxima of trangular wave small.
trang2=(2*abs(((x11+6)/p1)-np.floor(((x11+6)/p1)+0.5))-0.5)*0.5
trang3=(2*abs(((x22-m2_initial)/p2)-np.floor(((x22-m2_initial)/p2)+0.5))-0.5)*0.5
spring2,=plt.plot(x11,trang2)
spring3,=plt.plot(x22,trang3)
x=np.arange(m1_initial+(p/4),m2_initial-(p/4),0.01)
trang1=(2*abs(((x-m1_initial)/p)-np.floor(((x-m1_initial)/p)+0.5))-0.5)*0.5
spring1,=plt.plot(x,trang1)
#initial positions of dots to be animated
bluedot,=plt.plot(m1_initial,0,'bo',markersize=20)
reddot,=plt.plot(m2_initial,0,'ro',markersize=20)
start_time=time.time()
#function to update position of dots
def animate(i):
    m1_initial=-2+x1[i]
    m2_initial=2+x2[i]
    p1=(m1_initial+6)/4.5
    p2=(6-m2_initial)/4.5
    x11=np.arange(-6+(p1/4),m1_initial-(p1/4),0.01)
    x22=np.arange(m2_initial+(p2/4),6-(p2/4),0.01)
    trang2=(2*abs(((x11+6)/p1)-np.floor(((x11+6)/p1)+0.5))-0.5)*0.5
    trang3=(2*abs(((x22-m2_initial)/p2)-np.floor(((x22-m2_initial)/p2)+0.5))-0.5)*0.5
    p=(m2_initial-m1_initial)/4.5
    x=np.arange(m1_initial+(p/4),m2_initial-(p/4),0.01)
    trang1=(2*abs(((x-m1_initial)/p)-np.floor(((x-m1_initial)/p)+0.5))-0.5)*0.5
    spring1.set_data(x,trang1)
    spring2.set_data(x11,trang2)
    spring3.set_data(x22,trang3)
    reddot.set_data(m2_initial,0)
    bluedot.set_data(m1_initial,0)
    #time_elapsed=plt.legend(labels=['time',round(time.time() - start_time,2)],loc='upper right')
    #line above shows time passed as a legend but it also slows the program considerably so use it at your own risk
    return spring1,spring2,spring3,reddot,bluedot#,time_elapsed
#interval of 30 milisec don't work for some reason to complete 30 sec definde in t matrix
#20 millisec interval also takes around 35 sec to complete cycle of 30 sec
#but 10 millisec takes 11 sec to complete cycle of 30 sec idk why?
#blit makes animations smooth
#magic
myanime=animation.FuncAnimation(fig,animate,frames=len(t),interval=10,blit=True,repeat=False)
#writervideo=animation.FFMpegWriter(fps=60)
#myanime.save('coupledoscillator.mp4',writer=writervideo)
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))
