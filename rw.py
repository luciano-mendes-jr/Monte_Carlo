#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:10:59 2021

@author: luciano
"""
from statistics import mean 
from random import uniform 
 
NREP = 100000       #numero de vezes que o experimento é repetido 
NPAS = 50          #numero de passos do caminhante 
x , s = 0.0, 0.0    
p  = 0.9            #probabilidade de ir para a direita 
mi = 0.0 
xf = []  


#Simulação Monte-Carlo
for n in range(NREP):
    x = 0 
    for m in range(NPAS): #Passos do caminhante
        s = uniform(0,1)  
        if(s <= p):
            x = x + 1.0      
    xf.append(x) #Salva a quantidade de passos para direita
                 #de cada caminhante depois de NPAS passos. 

print("-=-"*18)  
print("Pr de ir para direita:               {}".format(p))
print("Número de Passos:                    {}".format(NPAS))
print("Número de Replicas de Monte Carlo:   {}".format(NREP))
print("Número médio de passos para direita: {}".format(mean(xf)))
print("Número médio de passos para direita: {}".format(NPAS*p)) 
print("-=-"*18)              
        


