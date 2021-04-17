#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:03:09 2021
@author: Luciano Mendes 
Description:  Realiza uma simulação de Monte Carlo p/ avaliar 
o viés do estimador do parâmetro que indexa a distribuição
exponencial. 
"""
#importa as funções de suas respectivas bibliotecas 
from math import  log 
from random import random, seed 
from statistics import mean, variance 

#função para gerar uma amostra aleatoria da exp 
#pelo método da inversão usando a inversa obtida 
#analiticamente 
def Exp(a, n): 
    x = [] #lista para guar os valores gerados
    for i in range(n): #laço para repetir o processo para n variaveis
        U = random()   #gerar U(0,1)
        IF = -log(1 - U)/a #expressão analitica da inversa 
        x.append(IF)       #guarda o valor gerado   
    return x #retorna a lista de valores gerados  

theta = 2.0 #define o valor do parametro da distribuiçao em questão
N = 100000  #número de replicas da amostra
Ta = 50     #tamanho da amostra
T = []      #será usada para guardar as estimativas

seed(1995, 2) #definie a semente e a versão do gerador 

for i in range(N): #laço de monte carlo 
    X = Exp(theta, Ta)      #gera uma amostra da exponencial 
    T.append(len(X)/sum(X)) #aplica o estimador na amostra  
    
vies = mean(T) - theta       #calcula o viés 
EQM = variance(T) + vies**2  #calcula o erro  quadratido médio 

#imprime os resultados  
print('θ       = {:.4f}'.format(theta))
print('E(T)    = {:.4f}'.format(mean(T)))
print('Viés(T) = {:.4f}'.format(vies))  
print('EQM(T)  = {:.4f}'.format(EQM)) 

