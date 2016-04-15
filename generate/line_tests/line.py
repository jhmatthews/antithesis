import py_read_output as r 
from pretty import *
import numpy as np 
import os, sys

set_pretty()
colors = get_colors()

s1 = r.read_spectrum("agn")
s2 = r.read_spectrum("agn_matom")
s3 = r.read_spectrum("agn7")

big_tick_labels(18)
figure(figsize=(10,6))
long_ticks()

for i in range(5,6):
	#subplot(6,1,i)
	plot(s1["Lambda"], s1[s1.colnames[9+(i)]], linewidth=2, label="Weight reduction")
	plot(s2["Lambda"], s2[s1.colnames[9+(i)]], linewidth=2, label="H \& He Macro-atoms")
	plot(s3["Lambda"], s3[s1.colnames[9+(i)]], linewidth=2, label="Simple-atoms")

xlabel("Wavelength (\AA)", fontsize=20)
ylabel("Flux (erg~s$^{-1}$~cm$^{-2}$~\AA$^{-1}$)", fontsize=18)
pretty_legend()
savefig("line_transfer_comparison.png", dpi=300)