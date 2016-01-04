##################################
#
# Makefile for latex with bibliography
#
##################################


DATE := $(shell date +'%y%m%d')

LCMD = latex
CMD = pdflatex


all:
	${CMD} Thesis
	bibtex Thesis
	${CMD} Thesis
	${CMD} Thesis
dv:
	${LCMD} Thesis
	bibtex Thesis
	${LCMD} Thesis
	${LCMD} Thesis
	dvips Thesis -o Thesis.ps
	ps2pdf Thesis.ps	
clean:	
	/bin/rm -f *.aux *.log *.dvi 

cleandates:
	/bin/rm -f *.dvi cvwinds*.pdf diffs*.pdf *.ps *.log *.aux


