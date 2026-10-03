## Importation of needed mathmatical tools
import numpy as np
import sympy as smp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
import os

## Definition of all symbols
t, g = smp.symbols('t g') #Definition of time and gravity symbols
m1, m2 = smp.symbols('m1 m2') #Definition of mass 1 and mass 2 symbols
L1, L2 = smp.symbols('L1 L2') #Definition of length 1 and length 2 symbols
the1, the2 = smp.symbols(r'\theta_1 \theta_2', cls = smp.Function) #Definition of theta 1 and theta 2 symbols

## Making the thetas functions of time
the1 = the1(t)
the2 = the2(t)

## Definition of the derivatives
the1_d = smp.diff(the1, t)
the2_d = smp.diff(the2, t)
the1_dd = smp.diff(the1_d, t)
the2_dd = smp.diff(the2_d, t)

## Definitions of x and y coordinates
x1 = -L1*smp.sin(the1)
y1 = -L1*smp.cos(the1)
x2 = -L1*smp.sin(the1) - L2*smp.sin(the2)
y2 = -L1*smp.cos(the1) - L2*smp.cos(the2)

## Definition of energy terms (kinetic and potential), implementation of the Legrangian (L = T - V)
K1 = 0.5*m1*((smp.diff(x1, t))**2 + (smp.diff(y1, t)**2)) #Kinetic energy of mass one
K2 = 0.5*m2*((smp.diff(x2, t))**2 + (smp.diff(y2, t)**2)) #Kinetic energy of mass two
U1 = m1*g*y1 #Potential energy of mass one
U2 = m2*g*y2 #Potential energy of mass two
T = smp.simplify(K1 + K2) #Total kinetic energy
V = smp.simplify(U1 + U2) #Total potential energy
L = smp.simplify(T - V) #Legrangian

## Euler-Legrange relationship
LE1 = smp.diff(L, the1) - smp.diff(smp.diff(L, the1_d), t).simplify() #Legrange formula for mass 1
LE2 = smp.diff(L, the2) - smp.diff(smp.diff(L, the2_d), t).simplify() #Legrange formula for mass 2

## Introduce a dummy variable, z1/z2, so that we can make it a first order ODE (Python cannot solve ODE's higher than the first order)
sols = smp.solve([LE1, LE2], (the1_dd, the2_dd), simplify = False, rational = False)
dz1dt_f = smp.lambdify((t, g, m1, m2, L1, L2, the1, the2, the1_d, the2_d), sols[the1_dd])
dz2dt_f = smp.lambdify((t, g, m1, m2, L1, L2, the1, the2, the1_d, the2_d), sols[the2_dd])                  
dthe1dt_f = smp.lambdify(the1_d, the1_d)
dthe2dt_f = smp.lambdify(the2_d, the2_d)
##print(dz1dt_f(2, 9.81, 1, 1, 1, 1, 4, 2, 5, 3), "rad/s^2")
##print(dz2dt_f(2, 9.81, 1, 1, 1, 1, 4, 2, 5, 3), "rad/s^2")

## Use the previous four functions to extract four first-order ODE's
def dSdt(S, t, g, m1, m2, L1, L2):
    the1, z1, the2, z2 = S
    return [
        dthe1dt_f(z1),
        dz1dt_f(t, g, m1, m2, L1, L2, the1, the2, z1, z2),
        dthe2dt_f(z2),
        dz2dt_f(t, g, m1, m2, L1, L2, the1, the2, z1, z2)
    ]

## Solve the ODE for different initial conditions
t = np.linspace(0, 40, 1001)
g = 9.81
m1 = 2
m2 = 1
L1 = 2
L2 = 1
ODE = odeint(dSdt, y0 = [3.14, 0, 3.14/4, 0], t = t, args = (g, m1, m2, L1, L2)) #Change these initial conditions to analyze different pendulum scenarios

# Plots of theta 1 and theta 2
the1 = ODE.T[0]
the2 = ODE.T[2]
plt.plot(t, the1, label = 'Theta 1')
plt.xlabel("time [s]")
plt.ylabel("Theta [rad]")
plt.plot(t, the2, label = "Theta 2")
plt.title("Theta versus Time")
plt.grid()
plt.legend()
plt.show()


#Plots of Kinetic and Potential Energy


## Obtaining x and y coordinates for the animation
def get_x1y1x2y2(t, the1, the2, L1, L2):
    return(L1*np.sin(the1), #returns x1
          -L1*np.cos(the1), #returns y1
           L1*np.sin(the1) + L2*np.sin(the2), #returns x2
          -L1*np.cos(the1) - L2*np.cos(the2)) #returns y2
x1, y1, x2, y2 = get_x1y1x2y2(t, ODE.T[0], ODE.T[2], L1, L2)


## Animation code
figure, ax = plt.subplots(1, 1, figsize = (8,8))
ax.set_title("Chaotic Double Pendulum Motion Analysis Using Legrangian Mechanics")
ax.set_facecolor ('k')
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ln1, = plt.plot([], [], 'ro--', lw = 3, markersize = 8)
trace1, = ax.plot([], [], color = 'green', lw = 0.5, alpha = 0.5)
trace2, = ax.plot([], [], color = 'white', lw = 0.5, alpha = 0.5)
ax.set_ylim(-5, 5)
ax.set_xlim(-5, 5)
def animate(i):
    ln1.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    trace1.set_data(x1[:i], y1[:i])
    trace2.set_data(x2[:i], y2[:i])
   
anim = animation.FuncAnimation(figure, animate, frames = 500, interval = 50)
anim.save('pen.gif', writer = 'pillow', fps = 25)
print(os.getcwd())