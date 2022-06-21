import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as odeint
import matplotlib.animation as animation
import time
fig, ax = plt.subplots()
def f(u,t):
    x=u[0]
    y=u[1]
    z=u[2]
    dx=10*(y-x)
    dy=x*(27-z)-y
    dz=x*y-(8/3)*z
    return [dx,dy,dz]
t=np.linspace(0,60,10000)
y0=[1,-1,2]
sol=odeint(f,y0,t)
X=sol[:,0]
Y=sol[:,1]
Z=sol[:,2]
plt.ylim(0,50)
plt.xlim(-20,20)
plt.xlabel('X')
plt.ylabel('Z')
#ax.plot(X,Z)
#plt.legend(['1st atom','2nd atom'],loc='upper right')
butterfly,=plt.plot(1,2)
start_time=time.time()
xdata,zdata=[],[]
def animate(i):
    xdata.append(X[i])
    zdata.append(Z[i])
    butterfly.set_data(xdata,zdata)
    return butterfly,
myanime=animation.FuncAnimation(fig,animate,frames=len(t),interval=1,blit=True,repeat=True)
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))
