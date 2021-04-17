#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:54:34 2021
@author: Luciano Mendes 
Description:  Realiza uma simulação de Monte Carlo p/ avaliar 
o viés do estimador do parâmetro que indexa a distribuição
exponencial.
"""
#importa as funções de suas respectivas bibliotecas  
from numpy.random import exponential, seed 
from statistics import mean, variance 

theta = 2.0 #define o valor do parametro da distribuiçao em questão
N = 100000  #número de replicas da amostra
Ta = 50     #tamanho da amostra
T = []      #será usada para guardar as estimativas

seed(1995) #define a semente 

for i in range(N): #laço de monte carlo
    X = exponential(1.0/theta, Ta) #gera uma amostra da exponencial 
    T.append(len(X)/sum(X))        #aplica o estimador na amostra
    
vies = mean(T) - theta #calcula o viés 
EQM = variance(T) + vies**2  #calcula o erro  quadratido médio 

#imprime os resultados  
print('θ       = {:.4f}'.format(theta))
print('E(T)    = {:.4f}'.format(mean(T)))
print('Viés(T) = {:.4f}'.format(vies))  
print('EQM(T)  = {:.4f}'.format(EQM)) 
   

