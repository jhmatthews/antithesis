from pylab import *
import numpy as np 
from constants import G, MSOL, C

rcParams["text.usetex"]="True"
a = np.arange(-1,1.001,0.001)

m = 1 

r = (m + np.sqrt(m**2 - a**2))#plot(a,r)
plot(a,r, c="k")


a = (np.arange(0,1.001,0.001))
term2 = ((1.0 + 2.0*a)**(1./3.))  + ((1.0 - 2.0*a)**(1./3.))
z1 = 1.0 + (((1 - (4.0 * a * a))**(1./3.)) * term2)
z2 = np.sqrt( (12.0*a*a) + z1**2)
r = (3.0 + z2 - np.sqrt((3 - z1) * (3.0 + z1 + 2.0 * z2)))
plot(2.0*a,r, c="k")
a = (np.arange(-1,0.001,0.001))
term2 = ((1.0 + 2.0*a)**(1./3.))  + ((1.0 - 2.0*a)**(1./3.))
z1 = 1.0 + (((1 - (4.0 * a * a))**(1./3.)) * term2)
z2 = np.sqrt( (12.0*a*a) + z1**2)
r = (3.0 + z2 + np.sqrt((3 - z1) * (3.0 + z1 + 2.0 * z2)))
plot(2.0*a,r, c="k")

text(0,6.6,"$R_{\mathrm{ISCO}}$", fontsize=20)
text(0,2.2,"$R_H$", fontsize=20)
ylabel("$R/(GM/c^2)$", fontsize=20)
xlabel("$a_*$", fontsize=20)
xlim(-0.998,0.998)
ylim(0,9)
savefig("risco.png", dpi=300)