import numpy as np

g = 9.81
m = 1000
def Forces(v, k=0):
    #This function calculates the instanteneous force on the cow, where the inputs are instanteneous
    #velocity (v) and the drag coefficient (k)
    return [-np.sign(v[0])*k*v[0]**2,-m*g-np.sign(v[1])*k*v[1]**2]


def Energy (r, v):
    #This function calculates the kinetic energy, potential energy, and total energy and will return them in that order
    #The arguments to this function are position (r), and velocity (v)
    KE=1/2*m*(v[0]**2+v[1]**2)
    PE=m*g*r[1]
    H=KE+PE
    return [KE, PE, H]

def Newpos(x,v,f,dt,time):
    a = [i/m for i in f]
    dx = x[0]+(v[0]+a[0]*time)*dt
    dy = x[1]+(v[1]+a[1]*time)*dt
    return [dx,dy]

def Newv(v, f, dt):
    return [v[0]+f[0]/m*dt,v[1]+f[1]/m*dt]