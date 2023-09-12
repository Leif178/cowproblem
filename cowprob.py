#This is the main file

from cowfunctions import *
import matplotlib.pyplot as plt
import numpy as np

##############################################################################
## Initial conditions

g=9.81 #gravitaional constant
k=.607 #drag constant

m=1000 # mass in kg
pos0=[0, 15] #initial posistion in meters
v0=[15.6464,0] #initial position in m/s
F0=[-np.sign(v0[0])*k*v0[0]**2,-np.sign(v0[1])*k*v0[1]**2-m*g] # initial force in N
KE0=1/2*m*(v0[0]**2+v0[1]**2) #Initial Kinetic Energy
PE0=m*g*pos0[1] #Initial Potential Energy
dt=0.01 #time step
t0=0

##############################################################################
## Iteration

xlist=[pos0]
vlist=[v0]
Flist=[F0]
Elist=[[KE0, PE0, KE0+PE0]]
time=[t0]

i=0
while xlist[i][1]>=0:
    
    xlist.append(Newpos(xlist[i],vlist[i],Flist[i],dt, time[i]))
    vlist.append(Newv(vlist[i],Flist[i],dt))
    Flist.append(Forces(vlist[i],k))
    Elist.append(Energy(xlist[i], vlist[i]))
    time.append(dt*i)
    i+=1
    
##############################################################################
## Plotting

x1=[xlist[i][0] for i in range(len(xlist))]
x2=[xlist[i][1] for i in range(len(xlist))]

plt.plot(x1,x2)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Trajectory')
plt.show()

KE = [Elist[i][0] for i in range(len(Elist))]
PE = [Elist[i][1] for i in range(len(Elist))]
H = [Elist[i][2] for i in range(len(Elist))]

plt.plot(time, KE, label='Kinetic Energy')
plt.plot(time, PE, label='Potential Energy')
plt.plot(time, H, label='Total Energy')
plt.title('Energy')
plt.xlabel('time (sec)')
plt.ylabel('joules')
plt.legend()
plt.show()