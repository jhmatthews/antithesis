#!/usr/bin/env python
from pylab import *
import py_read_output as r 
import py_plot_output as pl
import py_plot_util as util 
import os, sys 
from constants import *
import numpy as np
from pretty import *

set_pretty()
c= get_colors()

fnames = ["liner_template.ascii","ngc1068_template.ascii",
           "qso_template.ascii","seyfert1_template.ascii",
           "seyfert2_template.ascii"]

labels = ["LINER", "Quasar", "Sy 1", "Sy 2"]

fnames = ["liner_template.ascii",
           "qso_template.ascii","seyfert1_template.ascii",
           "seyfert2_template.ascii"]

figure(figsize=(10,14))
big_tick_labels(18)

for i, f in enumerate(fnames):

	subplot(4,1,i+1)

	w,flux = np.loadtxt(f, unpack=True)

	fnorm = util.get_flux_at_wavelength(w,flux,2000)

	plot(w,flux/fnorm, label=labels[i], linewidth=3, c='k')
	xlim(1000,7000)
	ylim(0.05,100.0)
	semilogy()

	#float_legend()
	text(6000,10,labels[i], fontsize=24)

	if i < 3:
		gca().set_xticklabels([])

	if i == 2:
		text(400,100,"$F / F_{2000}$", fontsize=24, rotation="vertical")

subplots_adjust(hspace=0, wspace=0, top=0.97, left=0.12, right=0.97, bottom=0.07)
xlabel("Wavelength (\AA)", fontsize=24)
savefig("../../figures/agn_templates.png", dpi=300)