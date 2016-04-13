import py_read_output as r 
from pretty import *
import numpy as np 
import os, sys

s1 = r.read_spectrum("agn")
s2 = r.read_spectrum("agn7")

figure(figsize=(8,12))

for i in range(1,7):
	subplot(6,1,i)
	plot(s1["Lambda"], s1[s1.colnames[9+(i)]], linewidth=2, label="Weight reduction")
	plot(s2["Lambda"], s2[s1.colnames[9+(i)]], linewidth=2, label="Indivisible (All Simple-atoms)")


savefig("line_transfer_comparison.png", dpi=300)