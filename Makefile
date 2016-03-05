##################################
#
# Makefile for latex with bibliography
#
##################################


DATE := $(shell date +'%y%m%d')

LCMD = latex
CMD = pdflatex


all:
	texcount -brief Chapters/Chapter1.tex Chapters/radtrans.tex Chapters/outflows.tex | tail -1
	${CMD} Thesis
	bibtex Thesis
	${CMD} Thesis
	${CMD} Thesis
	texcount -brief Chapters/Chapter1.tex Chapters/radtrans.tex Chapters/outflows.tex | tail -1
dv:
	texcount -brief Chapters/Chapter1.tex Chapters/radtrans.tex Chapters/outflows.tex | tail -1
	${LCMD} Thesis
	bibtex Thesis
	${LCMD} Thesis
	${LCMD} Thesis
	dvips Thesis -o Thesis.ps
	ps2pdf Thesis.ps
	texcount -brief Chapters/Chapter1.tex Chapters/radtrans.tex Chapters/outflows.tex | tail -1

wc:
	texcount -brief Chapters/Chapter1.tex Chapters/radtrans.tex Chapters/outflows.tex | tail -1
	texcount -brief Chapters/Chapter1.tex Chapters/radtrans.tex Chapters/outflows.tex Chapters/agnpaper.tex Chapters/cvpaper.tex Chapters/ewpaper.tex | tail -1

clean:	
	/bin/rm -f *.aux *.log *.dvi 

cleandates:
	/bin/rm -f *.dvi cvwinds*.pdf diffs*.pdf *.ps *.log *.aux


