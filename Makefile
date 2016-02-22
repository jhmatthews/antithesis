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
	texcount -brief Chapters/Chapter1.tex Chapters/radtrans.tex Chapters/accretion.tex Chapters/outflows.tex | tail -1
dv:
	${LCMD} Thesis
	bibtex Thesis
	${LCMD} Thesis
	${LCMD} Thesis
	dvips Thesis -o Thesis.ps
	ps2pdf Thesis.ps
	texcount -brief Chapters/Chapter1.tex Chapters/radtrans.tex Chapters/accretion.tex Chapters/outflows.tex | tail -1

clean:	
	/bin/rm -f *.aux *.log *.dvi 

cleandates:
	/bin/rm -f *.dvi cvwinds*.pdf diffs*.pdf *.ps *.log *.aux


