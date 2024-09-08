import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sci
from matplotlib.animation import FuncAnimation
#defining constants
g=9.8 #m/s**2
l=1#m
# equation of motion
def double_pendulum(u,t):
    theta1,theta2,omega1,omega2=u[0],u[1],u[2],u[3]
    H=np.array([[2,np.cos(theta2-theta1)],[np.cos(theta2-theta1),1]])
    H=np.linalg.inv(H)
    b=np.array([[(omega2**2)*np.sin(theta2-theta1)-2*(g/l)*np.sin(theta1)],[-(omega1**2)*np.sin(theta2-theta1)-(g/l)*np.sin(theta2)]])
    x=np.matmul(H,b)
    a1,a2=x[0,0],x[1,0]
    return [omega1,omega2,a1,a2]
# solving the eom with odeint
t=np.linspace(0,10,1000)
u0=[2,2,0,1]
u=sci.odeint(double_pendulum,u0,t)
def get_coords(theta):
    return (np.sin(theta),-np.cos(theta))
# animation of the double pendulum 
fig,ax=plt.subplots()
x01,y01=get_coords(u0[0])
x02,y02=get_coords(u0[1])
line1,=ax.plot([0,x01],[0,y01],lw=1,c='k')
follower1,=ax.plot(x01,y01,lw=0.5,c='k')
line2,=ax.plot([x01,x01+x02],[y01,y01+y02],lw=1,c='k')
follower2,=ax.plot(x02+x01,y02+y01,lw=0.5,c='r')
pend1=ax.add_patch(plt.Circle((x01,y01),0.03,fc='blue'))
pend2=ax.add_patch(plt.Circle((x01+x02,y01+y02),0.03,fc='blue'))
ax.set_xlim(-2.4,2.4)
ax.set_ylim(-2.4,2.4)
def animate(frame):
    x1,y1=get_coords(u[frame,0])
    x2,y2=get_coords(u[frame,1])
    line1.set_data([0,x1],[0,y1])
    line2.set_data([x1,x1+x2],[y1,y1+y2])
    pend1.set_center((x1,y1))
    pend2.set_center((x2+x1,y2+y1))
    x1,y1=get_coords(u[:frame,0])
    x2,y2=get_coords(u[:frame,1])
    follower1.set_data(x1,y1)
    follower2.set_data(x1+x2,y1+y2)

pendulum=FuncAnimation(fig,animate,frames=len(t),interval=1,repeat=True)

plt.show()
