# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:50:53 2021

@author: marce
"""

import random

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
        poblacion[pos]['pi'].append( pi)
        poblacion[pos]['qi'].append(sum_pi )
        pos = pos + 1
        
    return poblacion

def seleccion_elite (porcentaje, cant_pob, poblacion):

    padres_elite = []
    #cantidad a seleccionar por ejemplo 0,4 * 100
    K = int(porcentaje * cant_pob)
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

def seleccion_ruleta (porcentaje, cant_pob, poblacion):

    #cantidad a seleccionar por ejemplo 0,4 * 100
    K = int(porcentaje * cant_pob)
    padres_ruleta = []
    nro = []
    #genero K numeros al azar
    for i in range(K):
        nro.append(random.uniform(0, 1))
    nro = sorted(nro)
    #print('busco', nro)
    valor = nro.pop(0)
    for i in poblacion:
        qui = sum(i['qi'])
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

def seleccion_universal (porcentaje, cant_pob, poblacion):

    #cantidad a seleccionar por ejemplo 0,4 * 100
    K = int(porcentaje * cant_pob)
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

def seleccion_ranking (porcentaje, cant_pob, poblacion):
    
    padres_ranking = []
    
    
    list_desempenio = []    
    N = 0
    for i in poblacion:
        N = N + sum(i['desempenio'])
        list_desempenio.append(sum(i['desempenio']))        
    list_desempenio = sorted(list_desempenio,reverse=True)
    
    aux = []
    for i in list_desempenio:
        aux.append(((N - i)/N, i))
    
    # print(aux)
    # print(poblacion)
    return padres_ranking
    
def elijo_padres(poblacion, porcentaje, cant_pob, met_padres1, met_padres2):
 # TO DO 
 # Boltzmann
 # Torneos (ambas versiones)
 
    #Necesito las frecuencias relativas y acumuladas
    poblacion = calculo_pi(poblacion)
    
    padres = []

    if met_padres1 == 'elite':
        padres = seleccion_elite (porcentaje, cant_pob, poblacion)

    if met_padres1 == 'ruleta':
        padres = seleccion_ruleta (porcentaje, cant_pob, poblacion)

    if met_padres1 == 'universal':
        padres = seleccion_universal (porcentaje, cant_pob, poblacion)

    if met_padres1 == 'ranking':
        padres = seleccion_ranking(porcentaje, cant_pob, poblacion)

    if met_padres2 == 'elite':
        padres.extend(seleccion_elite (1 - porcentaje, cant_pob, poblacion))

    if met_padres2 == 'ruleta':
        padres.extend(seleccion_ruleta (1 - porcentaje, cant_pob, poblacion))

    if met_padres2 == 'universal':
        padres.extend(seleccion_universal (1 - porcentaje, cant_pob, poblacion))

    if met_padres2 == 'ranking':
        padres.extend(seleccion_ranking(1 - porcentaje, cant_pob, poblacion))

    return padres
