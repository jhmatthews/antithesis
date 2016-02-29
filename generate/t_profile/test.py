import disk_models as d
import numpy as np
import disk
import read_output as rd 
import py_plot_util as util
rd.setpars()

from pylab import *
from pretty import *
from constants import *

set_pretty()

def Ledd (m):

	'''
	calculates eddington luminosity for a solar mass m
	
	Args:
		m	mass in solar masses
	
	returns:
		Eddington luminosity in ergs s^-1, float
	'''
	
	m *= MSOL
	
	consts = (4.0 * PI * G * C * MPROT ) / THOMPSON
	
	L = consts * m
	
	return L


def mdot_from_edd ( edd, m , isco = 6.0):

	''' 
	calculates an accretion rate from an eddington fraction
	Args:
		edd_frac		eddington fraction
		m				mass of central object in solar masses
		isco 			ISCO radius in R_G 
	
	returns:
		mdot in solar masses / yr
	'''
	
	L = Ledd (m)		# eddington luminosity
	
	mdot = edd * L / ( (C ** 2) )
	
	mdot *= isco 
	
	mdot = mdot * ( YR ) / MSOL	# normalise units
	
	return mdot


masses = np.array([0.8, 1e9, 10.0])

rg = G * masses * MSOL / C / C
radii = np.array([7e8, 8.85e14, 8.85e6])
rgs = [7e8 / rg[0], 6, 6]

labels = ["WD", r"$10^9 M_\odot$ BH", r"$10 M_\odot$ BH"]
plt.rcParams["lines.linewidth"]  = 2
figure()




for i, m in enumerate(masses):
	mdot = mdot_from_edd(0.2, m , isco = rgs[i])

	rsa = disk.make_rings(3000,7000, m, mdot, radii[i], 1000 * radii[i], mode = "bb", nrings=500)
	plot( np.log10(rsa.r * radii[i]/ rg[i]), np.log10(rsa.T), label=labels[i])

float_legend()
ylabel("$\log (T_{\\rm eff} / K)$", fontsize = 16)
xlabel("$\log (R / R_{G})$", fontsize = 16)
#xlim(0,1.4)
#ylim(4,5)

savefig("disk_t.png", dpi=300)
#savefig("disk_t.eps",facecolor='w',edgecolor='w',bbox_inches='tight')




