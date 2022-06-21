import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as odeint
import matplotlib.animation as animation
import time
fig, ax = plt.subplots()
m1=1
m2=1
l1=1
l2=1
g=9.81
def f(u,t):
    ang1=u[0]
    dang1=u[1]
    ang2=u[2]
    dang2=u[3]
    dtheta1=u[1]
    #try not to blow up this differential equation because this differential equation has some singular points that only come into play for some values of m1,m2 and l1 for example try m1=1,m2=2,l1=0.5
    #singular points are at ((m1+m2)*l1^2)-(m2*l1*cos(theta1-theta2))=0
    d2theta1=(-1/(((m1+m2)*l1*l1)-(m2*l1*(np.cos(ang1-ang2)**2))))*((m2*l1*(dang1**2)*np.sin(ang1-ang2)*np.cos(ang1-ang2))-(m2*g*np.sin(ang2)*np.cos(ang1-ang2))+(m2*l2*(dang2**2)*np.sin(ang1-ang2))+(g*(m1+m2)*np.sin(ang1)))
    dtheta2=u[3]
    d2theta2=(1/(m2*l2))*(-(m2*l1*d2theta1*np.cos(ang1-ang2))+(m2*l1*(dang1**2)*np.sin(ang1-ang2))-(m2*g*np.sin(ang2)))
    return [dtheta1,d2theta1,dtheta2,d2theta2]
t=np.linspace(0,100,10000)
m1_initial=1
m2_initial=1.5
y0=[m1_initial,0,m2_initial,0]
sol=odeint(f,y0,t)
theta1=sol[:,0]
theta2=sol[:,2]
#plt.subplot(2,1,1)
#plt.plot(t,theta1)
#plt.ylabel("\u03b8\u2081")
#plt.subplot(2,1,2)
#plt.plot(t,theta2)
#plt.ylabel("\u03b8\u2082")
#plt.xlabel("time(s)")
#plt.plot(theta1,theta2)
plt.xlim(-l1-l2-1,l1+l2+1)
plt.ylim(-l1-l2-1,1)
bluedot,=plt.plot(l1*np.sin(m1_initial),-l1*np.cos(m1_initial),'bo')
reddot,=plt.plot((l1*np.sin(m1_initial))+(l2*np.sin(m2_initial)),-(l1*np.cos(m1_initial))-(l2*np.cos(m2_initial)),'ro')
x2_values=[l1*np.sin(m1_initial),(l1*np.sin(m1_initial))+(l2*np.sin(m2_initial))]
y2_values=[-l1*np.cos(m1_initial),-(l1*np.cos(m1_initial))-(l2*np.cos(m2_initial))]
x1_values=[0,x2_values[0]]
y1_values=[0,y2_values[0]]
supportx=[-1,1]
supporty=[0,0]
plt.plot(supportx,supporty,'k',linewidth=2)
line1,=plt.plot(x1_values,y1_values)
line2,=plt.plot(x2_values,y2_values)
start_time=time.time()
def animate(i):
    x2_values=[l1*np.sin(theta1[i]),(l1*np.sin(theta1[i]))+(l2*np.sin(theta2[i]))]
    y2_values=[-l1*np.cos(theta1[i]),-(l1*np.cos(theta1[i]))-(l2*np.cos(theta2[i]))]
    #checking if length of second rod is staying same or not because on graph it sometimes look like it is not staying same.if l2 is 3 than print show give us 9
    #print(((x2_values[1]-x2_values[0])**2)+((y2_values[1]-y2_values[0])**2))
    #ok the reason it was looking looke the rod is not the same legth because scale of x and y axis is different
    x1_values=[0,x2_values[0]]
    y1_values=[0,y2_values[0]]
    line1.set_data(x1_values,y1_values)
    line2.set_data(x2_values,y2_values)
    bluedot.set_data(x2_values[0],y2_values[0])
    reddot.set_data(x2_values[1],y2_values[1])
    return line1,line2,reddot,bluedot
myanime=animation.FuncAnimation(fig,animate,frames=len(t),interval=10,blit=True,repeat=False)
plt.show()    
print("--- %s seconds ---" % (time.time() - start_time))