from pylab import *
import numpy as np 
from constants import G, MSOL, C
import astropy.io.fits as pyfits
from py_plot_util import smooth

figure(figsize=(10,8))
rcParams["text.usetex"]="True"

flux, d, dd = np.loadtxt("zeta_pup.txt", unpack=True)

w = 1150.0 + np.arange(16500) * 0.05


mask = (flux > 0)
plot(w[mask],1e7*smooth(flux[mask]), c="k", linewidth=2.5)

#text(0,6.6,"$R_{\mathrm{ISCO}}$", fontsize=20)
#text(0,2.2,"$R_H$", fontsize=20)
ylabel("Flux ($10^{-7}$~erg~s$^{-1}$~cm$^{-2}$~\AA$^{-1}$)", fontsize=20)
xlabel("Wavelength (\AA)", fontsize=20)
#xlim(-0.998,0.998)
ylim(0,1)
subplots_adjust(bottom=0.1)
xlim(1150,1900)
savefig("zeta_pup.png", dpi=300)