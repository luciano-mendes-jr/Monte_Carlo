#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 21:16:12 2021
@author: Luciano Mendes 
Description:  Realiza uma simulação de Monte Carlo p/ avaliar 
o viés do estimador dos parâmetros que indexa a distribuição
Gama. Tal estimador é obtido atrás da aplicação do método dos 
momentos. 
"""
#importa as funções de suas respectivas bibliotecas 
from matplotlib.pylab import plot, arange, grid, legend
from scipy.optimize import fsolve
from statistics import mean
from numpy.random import gamma
import math as mt

#variaveis globais para armazenar os momentos amostrais 1 e 2 
x1, x2 = 0.0 , 0.0 

#expressão da densidade da gamma  
def gama(a,b,x):
    f = []
    g = mt.gamma(a) 
    for i in x:
        e = mt.exp(-1*b*i)
        f.append(((b**a)*e*(i**(a-1)))/g)
    return (f) 
    
#sistema obtido pelo método dos momentos 
def sistema(p):
    a, b = p 
    eq1  = x1 -  a*b  
    eq2  = x2 - (a*b**2)*(1.0 + a)
    return [eq1, eq2]

#listas onde serão guardas as estimativas de alfa e beta 
beta, alfa = [], [] 
 
#parametros da gamma 
a = 3.0 #alfa 
b = 1.0 #beta

n = 300   #tamanho da amostra
N = 10000 #numero de replicas da amostra 

for k in range(N):
    
    X  = gamma(a, b, n) #gera uma amostra de tamanho n, X ~ gama(a,b)
    x1 = mean(X)    #calcula o primeiro momento amostral 
    x2 = mean(X**2) #calcula o segundo momento amostral  
    s  = fsolve(sistema, (x1,x1)) #Resolve o Sistema 
    alfa.append(s[0]) #Guarda a estimativa de alfa
    beta.append(s[1]) #Guarda a estimativa de beta 

m_a = mean(alfa) #calcula as médias das estimativas 
m_b = mean(beta) #calcula as médias das estimativas 
vies_a = m_a - a  #calcula o viés de alfa
vies_b = m_b - b  #calcula o viés de beta
print('\n'*4) #pula 4 linhas  
#imprime os resultados 
print("α                           = {:.4f}".format(a))
print("β                           = {:.4f}".format(b))
print("Média das estimativas de α  = {:.4f}".format(mean(alfa)))
print("Média das estimativas de β  = {:.4f}".format(mean(beta)))
print("Viés das estimativas de α   = {:.4f}".format(vies_a))
print("Viés das estimativas de β   = {:.4f}".format(vies_b))

#gera o suporte da distribuição
x  = arange(0, max(X), 0.0001)

#calcula os valores da distribuição no suporte para
y  = gama(a,b,x) #os parametros verdadeis 
y2 = gama(m_a,m_b,x) #os parametros 

#plota o grafico da desidade da gamma com os parametros 
#reais e estimados 
plot(x,y,lw = 3,color = 'black', label = "Curva Teórica") 
plot(x,y2,lw = 3,color = 'orange', label = "Curva Estimada") 
grid(color = 'grey', ls = '--', lw = 1.0)
legend(fontsize=15)
 

