from pylab import *
import numpy as np 
from constants import G, MSOL, C

RG = G * 10.0 * MSOL / C / C
x = np.arange(1.2,3.0,0.01)
x2 = np.arange(1,3.0,0.01)
r = x * RG
r2 = x2 * RG

vlines([1.2], 0,10000, linestyle="--")
omega = np.sqrt(G * 10.0 * MSOL / r / r / r)
plot(x, omega, c="k")

omega2 = np.sqrt(G * 10.0 * MSOL / r2 / r2 / r2) 
plot(x2, omega2, ls="--", c="k")

show() 