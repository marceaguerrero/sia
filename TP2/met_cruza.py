# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 00:30:14 2021

@author: marce
"""

import random
import seleccion_padres
import calculos

def un_punto(padres, armas, botas, cascos, guantes, pecheras):
    
    nuevos_hijos = []
    
    while (padres):
        
        if (not padres):
            break
        papa = padres.pop(0)
        if (not padres):
            break
        mama = padres.pop(0)


        #elijo un locus al azar que es un valor entre 0 y el tamanio del gen        
        locus = int(random.uniform(0, 31))
        #intercambio genes de padre y madre en ese locus
        altura = papa['altura'][0][:locus]+mama['altura'][0][locus:]
        idx_armas = papa['idx_armas'][0][:locus]+mama['idx_armas'][0][locus:]      
        idx_botas = papa['idx_botas'][0][:locus]+mama['idx_botas'][0][locus:]
        idx_cascos = papa['idx_cascos'][0][:locus]+mama['idx_cascos'][0][locus:]
        idx_guantes = papa['idx_guantes'][0][:locus]+mama['idx_guantes'][0][locus:]
        idx_pecheras = papa['idx_pecheras'][0][:locus]+mama['idx_pecheras'][0][locus:]

        if calculos.bin_to_float(idx_armas) > 999999: idx_armas = calculos.float_to_bin(0)
        if calculos.bin_to_float(idx_botas) > 999999: idx_botas = calculos.float_to_bin(0)
        if calculos.bin_to_float(idx_cascos) > 999999: idx_cascos = calculos.float_to_bin(0)
        if calculos.bin_to_float(idx_guantes) > 999999: idx_guantes = calculos.float_to_bin(0)
        if calculos.bin_to_float(idx_pecheras) > 999999: idx_pecheras = calculos.float_to_bin(0)

        jugador = {'clase': [], 'altura': [], 'desempenio': [], 
                  'pi': [], 'qi': [],
                   'idx_armas': [], 'idx_botas': [],
                   'idx_cascos': [], 'idx_guantes': [],
                   'idx_pecheras': []}
        
        jugador['clase'].append(papa['clase'][0])
        jugador['altura'].append(altura)
        # print('progenitores', papa, mama)
        # print( 'altura ' , altura)
        
        prom_altura = calculos.bin_to_float(altura)
        atm = 0.7 - ((prom_altura*3)-5)**4 + ((prom_altura*3)-5)**2 + (prom_altura/4)
        dem = 1.9 + ((prom_altura*2.5) - 4.16)**4 - ((prom_altura*2.5) - 4.16)**2 - ((prom_altura*3)/10)
        #genero_desempeño
        fuerza, agilidad, pericia, resistencia, vida = calculos.calculo_items(calculos.bin_to_float(idx_armas), 
                                                                     calculos.bin_to_float(idx_botas), 
                                                                     calculos.bin_to_float(idx_cascos), 
                                                                     calculos.bin_to_float(idx_guantes), 
                                                                     calculos.bin_to_float(idx_pecheras), armas, botas, cascos, guantes, pecheras)
        ataque = (agilidad + pericia) * fuerza * atm
        defensa = (resistencia + pericia) * vida * dem
        desempenio = calculos.calculo_desempenio (jugador['clase'], ataque, defensa)

        jugador['desempenio'].append(desempenio) 
        jugador['idx_armas'].append(idx_armas)
        jugador['idx_botas'].append(idx_botas)
        jugador['idx_cascos'].append(idx_cascos)
        jugador['idx_guantes'].append(idx_guantes)
        jugador['idx_pecheras'].append(idx_pecheras)
        nuevos_hijos.append(jugador)


    nuevos_hijos = seleccion_padres.calculo_pi(nuevos_hijos)

    return nuevos_hijos

def cruza (met_cruza, padres,armas, botas, cascos, guantes, pecheras):
# 2 PUNTOS
# ANULAR
# UNIFORME
    nuevos_hijos = [] 
    if met_cruza == '1 punto':
        nuevos_hijos = un_punto(padres,armas, botas, cascos, guantes, pecheras)

    return nuevos_hijos

