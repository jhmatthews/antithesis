##################################
#
# Makefile for latex with bibliography
#
##################################


DATE := $(shell date +'%y%m%d')

CMD = latex
PCMD = pdflatex


all:
	${CMD} Thesis
	bibtex Thesis
	${CMD} Thesis
	${CMD} Thesis
	dvips Thesis -o Thesis.ps
	ps2pdf Thesis.ps	
clean:	
	/bin/rm -f *.aux *.log *.dvi 

cleandates:
	/bin/rm -f *.dvi cvwinds*.pdf diffs*.pdf *.ps *.log *.aux


