import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sci
from matplotlib.animation import FuncAnimation
#defining constants
g=9.8 #m/s**2
l=1#m
u0=[1,0]#rad
alpha=1

def pendulum_wo_friction(x,t):
    return [x[1],-(g/l)*np.sin(x[0])]
def pendulum_w_friction(x,t):
    return [x[1],-(alpha/l)*x[1]-(g/l)*np.sin(x[0])]

#solving the differential equations with odeint
t=np.linspace(0,10,300)
#u=sci.odeint(pendulum_w_friction,u0,t)
u=sci.odeint(pendulum_wo_friction,u0,t)

#plotting the angle and the nagular velocity with respect to time
plt.plot(t,u[:,0],label='theta',color='b')
plt.plot(t,u[:,1],label='omega',color='r')
plt.grid()
plt.legend()
plt.show()

#plotting the phase protrati ,the angular velocity with respect to the velocity
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
L=max(u[:,0])+2
d=max(u[:,1])+2
plt.xlim(-L,L)
plt.ylim(-d,d)
plt.plot(u[:,0],u[:,1],label='portrait de phase',color='y')
plt.grid()
plt.show()

def get_coords(theta):
    return (np.sin(theta),-np.cos(theta))
#the animation of a single pendulum
fig,ax=plt.subplots()
x0,y0=get_coords(u0[0])
line,=ax.plot([0,x0],[0,y0],lw=0.5,c='k')
pend=ax.add_patch(plt.Circle((x0,y0),0.02,color='blue'))
ax.set_xlim(-1.2*l,1.2*l)
ax.set_ylim(-1.2*l,1.2*l)
def animate(frame):
    x,y=get_coords(u[frame,0])
    line.set_data([0,x],[0,y])
    pend.set_center((x,y))

one_pendulum=FuncAnimation(fig,animate,frames=len(t),interval=30,repeat=True)

plt.show()
