#!/usr/bin/env python

test_cases = [(('pedra', 'tesoura'),'pedra'),(('papel' , 'tesoura') , 'tesoura') , (('pedra', 'papel'), 'papel'),(('papel', 'papel'), 'empate'), (('pedra' , 'pedra'),'empate') , (('tesoura', 'tesoura') , 'empate' ), (('tesoura', 'pedra'),'pedra'), (('tesoura' , 'papel') , 'tesoura'), (('papel', 'pedra'), 'papel')]
#teste1 j1 = pedra   j2 = tesoura 
#teste2 j1 = papel   j2 = tesoura
#teste3 j1 = pedra   j2 = papel
#teste4 j1 = papel   j2 = papel
#teste5 j1 = pedra   j2 = pedra
#teste6 j1 = tesoura j2 = tesoura
#teste7 j1 = tesoura j2 = pedra
#teste8 j1 = tesoura j2 = papel
#teste9 j1 = papel   j2 = pedra
def jokenpo(j1, j2):
		
	if(j1=='pedra' and j2=='tesoura')or (j1=='tesoura' and j2=='pedra'):
		return 'pedra'
	if(j1=='papel' and j2=='tesoura')or (j1=='tesoura' and j2=='papel'):	
		return 'tesoura'
        if(j1=='pedra' and j2=='papel')or (j1=='papel' and j2=='pedra'):
		return 'papel'


	return 'empate'
	
