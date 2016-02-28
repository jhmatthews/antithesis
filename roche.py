from constants import *
import numpy as np
from pylab import *


def get_omega(a, m):

	o = np.sqrt(G * m / a**3)

	return np.array([0,0,o])

def vec_diff(v1, v2):

	dx = v1[0] - v2[0]
	dy = v1[1] - v2[1]

	return np.sqrt(dx*dx + dy*dy)


def roche(x, y, a, m1, m2):

	m = m2 / (m1+m2)

	omega = get_omega(a, m)

	term1 = G * m1 / np.sqrt( (x - m*a)**2 + y*y)

	term2 = G * m2 / np.sqrt( (x + a - m*a)**2 + y*y)

	term3 = omega*omega*np.sqrt(x*x + y*y)

	return -term1-term2-term3


x = np.arange(-1000,1000,0.1) * 1e4
y = np.arange(-1000,1000,0.1) * 1e4
q = 0.25
m1 = 1. * MSOL 
m2 = m1 / q 
phi = np.zeros([len(x), len(y)])
a = 1e6

for i in range(len(x)):
	for j in range(len(y)):
		phi[i,j] = roche(x[i], y[i], a, m1, m2) 




