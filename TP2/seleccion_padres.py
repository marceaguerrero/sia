# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:50:53 2021

@author: marce
"""

import random
# para boltzmann por la variable e
import math

def calculo_pi(poblacion):

    sum_total = 0
    for i in poblacion:
        sum_total = sum_total + sum(i['desempenio'])
    
    pi = 0
    sum_pi = 0 
    pos = 0 
    for i in poblacion:
        pi = sum(i['desempenio']) / sum_total
        sum_pi = sum_pi + pi
        poblacion[pos]['pi'] =  pi
        poblacion[pos]['qi'] = sum_pi 
        pos = pos + 1
        
    return poblacion

def seleccion_elite (K, poblacion):

    padres_elite = []
    #cantidad a seleccionar por ejemplo 0,4 * 100
    K = int(K)
    #tengo que ordenar y obtener los K con mejor valor
    list_desempenio = []    
    for i in poblacion:
        list_desempenio.append(sum(i['desempenio']))        
    elite = sorted(list_desempenio,reverse=True)
    elite = elite[:K]    
    #ahora busco en el diccionario esos desempenios y armo la lista de padres
    for i in elite:
        padres_elite.append(next((sub for sub in poblacion if sum(sub['desempenio']) == i), None))
     
    return padres_elite

def seleccion_ruleta (K, poblacion):

    #cantidad a seleccionar por ejemplo 0,4 * 100
    K = int(K)
    padres_ruleta = []
    nro = []
    #genero K numeros al azar
    for i in range(K):
        nro.append(random.uniform(0, 1))
    nro = sorted(nro)
    #print('busco', nro)
    valor = nro.pop(0)
    for i in poblacion:
        qui = (i['qi'])
        #print('qui ', qui)
        if valor <= qui:        
            #print(i, nro)
            padres_ruleta.append(i)
            if (nro):
                valor = nro.pop(0)
            else:
                break
    
    #print('ruleta', padres_ruleta)
    #busco en qi esos numeros y listo bye bye
    return padres_ruleta

def seleccion_torneo_det(K, cant_pob, poblacion):
    K = int(K)
    padres_torneo_det = []

    #se elije un valor M
    M = int(cant_pob/3)

    list_desempenio = []    
    list_aux = []
    for i in poblacion:
        list_desempenio.append(i['desempenio'])        
        
    while (len(padres_torneo_det) < K):
        list_aux = random.sample(list_desempenio, M)
        list_aux = sorted(list_aux,reverse=True)  
        i = list_aux.pop(0)   
        padres_torneo_det.append(next((sub for sub in poblacion if sub['desempenio'] == i), None))
    
    return padres_torneo_det
    

def seleccion_torneo_prob (K, cant_pob, poblacion):
    K = int(K)
    padres_torneo_prob = []
    
   
    list_desempenio = []    
    list_aux = []
    
    for i in poblacion:
        list_desempenio.append(i['desempenio'])        

        
    while (len(padres_torneo_prob) < K):
        threshold= random.uniform(0.5,1)
        list_aux = random.sample(list_desempenio, 2)
        list_aux = sorted(list_aux,reverse=True)  
        r = random.uniform(0,1)
        if r < threshold:
            #selecciono el mas apto
            i = list_aux.pop(0)               
            padres_torneo_prob.append(next((sub for sub in poblacion if sub['desempenio'] == i), None))
        
        else:
            #selecciono el otro
            i = list_aux.pop()               
            padres_torneo_prob.append(next((sub for sub in poblacion if sub['desempenio'] == i), None))
    
    
    return padres_torneo_prob

def seleccion_universal (K, poblacion):

    #cantidad a seleccionar por ejemplo 0,4 * 100
    K = int(K)
    padres_universal = []
    un_nro = random.uniform(0, 1)
    nro = []
    #genero K numeros al azar
    for i in range(K):
        nro.append((un_nro + i)/K)
    nro = sorted(nro)
    #print('busco', nro)
    valor = nro.pop(0)
    for i in poblacion:
        qui = sum(i['qi'])
        #print('qui ', qui)
        if valor <= qui:        
            #print(i, nro)
            padres_universal.append(i)
            if (nro):
                valor = nro.pop(0)
            else:
                break
    
    #print('universal', padres_universal)
    #busco en qi esos numeros y listo bye bye
    return padres_universal

def seleccion_ranking (K, poblacion):
    
    padres_ranking = []
    K = int(K) 
    
    list_desempenio = []    
    N = 0
    for i in poblacion:
        N = N + sum(i['desempenio'])
        list_desempenio.append(sum(i['desempenio']))        
    list_desempenio = sorted(list_desempenio,reverse=True)
    
    aux = []
    for i in list_desempenio:
        aux.append(((N - i)/N, i))
    
    #luego se usa ruleta con esa nueva f
    
    valor = aux.pop(0)
    cant = 0
    qui = 0 
    for i in poblacion:
       
        qui = float(i['qi'])
        if float(valor[0]) <= qui:        
            #print(i, nro)
            padres_ranking.append(i)
            cant = cant + 1
            if cant >= K:
                break
            if (aux):
                valor = aux.pop(0)
            else:
                break
 
    return padres_ranking
    
def seleccion_boltzmann(porcentaje, K, poblacion):

    padres_boltzmann = []
    K = int(K) 
    
    list_desempenio = []    
    N = 0
    T = 0.99
    for i in poblacion:
        #T = T * 0.1
        N = N + math.exp(float(i['desempenio'][0]) / T)

    N = N / len(poblacion)
    
    for i in poblacion:
        #T = T * 0.1
        x = math.exp(float(i['desempenio'][0]) / T) / N
        list_desempenio.append(x)        
    list_desempenio = sorted(list_desempenio,reverse=True)
      
    #luego se usa ruleta con esa nueva f
    
    valor = list_desempenio.pop(0)
    cant = 0
    qui = 0 
    for i in poblacion:
        
        qui = float(i['qi'])
        if float(valor) <= qui:        
            padres_boltzmann.append(i)
            cant = cant + 1
            if cant >= K:
                break
            if (list_desempenio):
                valor = list_desempenio.pop(0)
            else:
                break
 
    return padres_boltzmann

def elijo_padres(poblacion, porcentaje, cant_pob, K, met_padres1, met_padres2):
 # TO DO 
 # Boltzmann

    #Necesito las frecuencias relativas y acumuladas
    poblacion = calculo_pi(poblacion)
    
    padres = []

    if met_padres1 == 'elite':
        padres = seleccion_elite (porcentaje * K, poblacion)

    if met_padres1 == 'ruleta':
        padres = seleccion_ruleta (porcentaje * K, poblacion)

    if met_padres1 == 'universal':
        padres = seleccion_universal (porcentaje * K, poblacion)

    if met_padres1 == 'ranking':
        padres = seleccion_ranking(porcentaje * K, poblacion)

    if met_padres1 == 'torneo_det':
        padres = seleccion_torneo_det(porcentaje * K, cant_pob, poblacion)

    if met_padres1 == 'torneo_prob':
        padres = seleccion_torneo_prob(porcentaje * K, cant_pob, poblacion)

    if met_padres1 == 'boltzmann':
        padres = seleccion_boltzmann(porcentaje * K, cant_pob, poblacion)

    if met_padres2 == 'elite':
        padres.extend(seleccion_elite ((1 - porcentaje) * K, poblacion))

    if met_padres2 == 'ruleta':
        padres.extend(seleccion_ruleta ((1 - porcentaje) * K, poblacion))

    if met_padres2 == 'universal':
        padres.extend(seleccion_universal ((1 - porcentaje) * K, poblacion))

    if met_padres2 == 'ranking':
        padres.extend(seleccion_ranking((1 - porcentaje) * K, poblacion))

    if met_padres2 == 'torneo_det':
        padres.extend(seleccion_torneo_det((1 - porcentaje) * K, cant_pob, poblacion))

    if met_padres2 == 'torneo_prob':
        padres.extend(seleccion_torneo_prob((1 - porcentaje) * K, cant_pob, poblacion))

    if met_padres2 == 'boltzmann':
        padres.extend(seleccion_boltzmann((1 - porcentaje) * K, cant_pob, poblacion))

    return padres
