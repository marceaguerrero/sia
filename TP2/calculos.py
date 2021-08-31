# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:11:43 2021

@author: marce
"""
import struct
import math

def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def calculo_items(idx_armas, idx_botas, idx_cascos, idx_guantes, idx_pecheras, 
                  armas, botas, cascos, guantes, pecheras):
    
    #id	Fu	Ag	Ex	Re	Vi
    fuerza_total = 0    
    fuerza = 0
    idx_armas = int(idx_armas)
    idx_botas = int(idx_botas)
    idx_cascos = int(idx_cascos)
    idx_guantes = int(idx_guantes)
    idx_pecheras = int(idx_pecheras)
    # print('idx_armas ', int(idx_armas))
    # print('armas[idx_armas][1]', armas[idx_armas][1])
    # 
    # print(idx_armas)
    # print(idx_botas)
    # print(idx_cascos)
    # print(idx_guantes)
    # print(idx_pecheras)

    # print( armas[idx_armas][1])
    # print( botas[idx_botas][1])
    # print( cascos[idx_cascos][1])
    # print( guantes[idx_guantes][1])
    # print( pecheras[idx_pecheras][1])

    fuerza_total = fuerza_total + float(armas[idx_armas][1])
    fuerza_total = fuerza_total + float(botas[idx_botas][1])
    fuerza_total = fuerza_total + float(cascos[idx_cascos][1])
    fuerza_total = fuerza_total + float(guantes[idx_guantes][1])
    fuerza_total = fuerza_total + float(pecheras[idx_pecheras][1])
    fuerza = 100 * math.tanh(0.01 * fuerza_total)

    agilidad_total = 0    
    agilidad = 0
    agilidad_total = agilidad_total + float(armas[idx_armas][2])
    agilidad_total = agilidad_total + float(botas[idx_botas][2])
    agilidad_total = agilidad_total + float(cascos[idx_cascos][2])
    agilidad_total = agilidad_total + float(guantes[idx_guantes][2])
    agilidad_total = agilidad_total + float(pecheras[idx_pecheras][2])
    agilidad = math.tanh(0.01 * agilidad_total)

    pericia_total = 0    
    pericia = 0
    pericia_total = pericia_total + float(armas[idx_armas][3])
    pericia_total = pericia_total + float(botas[idx_botas][3])
    pericia_total = pericia_total + float(cascos[idx_cascos][3])
    pericia_total = pericia_total + float(guantes[idx_guantes][3])
    pericia_total = pericia_total + float(pecheras[idx_pecheras][3])
    pericia = 0.6 * math.tanh(0.01 * pericia_total)

    resistencia_total = 0    
    resistencia = 0
    resistencia_total = resistencia_total + float(armas[idx_armas][4])
    resistencia_total = resistencia_total + float(botas[idx_botas][4])
    resistencia_total = resistencia_total + float(cascos[idx_cascos][4])
    resistencia_total = resistencia_total + float(guantes[idx_guantes][4])
    resistencia_total = resistencia_total + float(pecheras[idx_pecheras][4])
    resistencia = math.tanh(0.01 * resistencia_total)

    vida_total = 0    
    vida = 0
    vida_total = vida_total + float(armas[idx_armas][5])
    vida_total = vida_total + float(botas[idx_botas][5])
    vida_total = vida_total + float(cascos[idx_cascos][5])
    vida_total = vida_total + float(guantes[idx_guantes][5])
    vida_total = vida_total + float(pecheras[idx_pecheras][5])
    vida = 100 * math.tanh(0.01 * vida_total)

    return fuerza, agilidad, pericia, resistencia, vida 

def calculo_desempenio (clase, ataque, defensa):
    
    if len(clase[0]) > 1:
        clase = clase[0]
        
    if (clase == 'guerrero'):
        return (0.6 * ataque) + (0.6 * defensa)

    if (clase == 'arquero'):
        return (0.9 * ataque) + (0.1 * defensa)
    
    if (clase == 'defensor'):
        return (0.3 * ataque) + (0.8 * defensa)

    if (clase == 'infiltrado'):
        return (0.8 * ataque) + (0.3 * defensa)

    return 0
   
    
def guardar(ronda, poblacion):
    
    minimo = 100
    cant = 1
    suma =0
    for i in poblacion:
        if minimo > float(i['desempenio'][0]):
            minimo = float(i['desempenio'][0])
        suma = suma + float(i['desempenio'][0])
        cant = cant + 1
        
    return minimo, suma/cant , ronda

