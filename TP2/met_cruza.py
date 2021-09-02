# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 00:30:14 2021

@author: marce
"""

import random
import seleccion_padres
import calculos
import numpy as np

def un_punto(padres, armas, botas, cascos, guantes, pecheras):
    
    nuevos_hijos = []
    
    while (padres):
        
        if (not padres):
            break
        papa = padres.pop(0)
        if (not padres):
            break
        mama = padres.pop(0)
        padres.insert(0, mama)

        #elijo un locus al azar que es un valor entre 0 y el tamanio del gen        
        locus = int(random.uniform(1,6))
        #intercambio genes de padre y madre en ese locus para cada hijo

        #lleno hijo 1
        jugador1 = {'clase': [], 'altura': [], 'desempenio': [], 
                  'pi': [], 'qi': [],
                   'idx_armas': [], 'idx_botas': [],
                   'idx_cascos': [], 'idx_guantes': [],
                   'idx_pecheras': []}
        jugador2 = {'clase': [], 'altura': [], 'desempenio': [], 
                  'pi': [], 'qi': [],
                   'idx_armas': [], 'idx_botas': [],
                   'idx_cascos': [], 'idx_guantes': [],
                   'idx_pecheras': []}
        
        jugador1['clase'].append(papa['clase'][0])
        jugador2['clase'].append(papa['clase'][0])

        if locus == 1:
            jugador1['altura'].append(papa['altura'][0])
            jugador2['altura'].append(mama['altura'][0])
            jugador1['idx_armas'].append(mama['idx_armas'][0])
            jugador2['idx_armas'].append(papa['idx_armas'][0])
            jugador1['idx_botas'].append(mama['idx_botas'][0])
            jugador2['idx_botas'].append(papa['idx_botas'][0])
            jugador1['idx_cascos'].append(mama['idx_cascos'][0])
            jugador2['idx_cascos'].append(papa['idx_cascos'][0])
            jugador1['idx_guantes'].append(mama['idx_guantes'][0])
            jugador2['idx_guantes'].append(papa['idx_guantes'][0])
            jugador1['idx_pecheras'].append(mama['idx_pecheras'][0])
            jugador2['idx_pecheras'].append(papa['idx_pecheras'][0])
        if locus == 2:
            jugador1['altura'].append(papa['altura'][0])
            jugador2['altura'].append(mama['altura'][0])
            jugador1['idx_armas'].append(papa['idx_armas'][0])
            jugador2['idx_armas'].append(mama['idx_armas'][0])
            jugador1['idx_botas'].append(mama['idx_botas'][0])
            jugador2['idx_botas'].append(papa['idx_botas'][0])
            jugador1['idx_cascos'].append(mama['idx_cascos'][0])
            jugador2['idx_cascos'].append(papa['idx_cascos'][0])
            jugador1['idx_guantes'].append(mama['idx_guantes'][0])
            jugador2['idx_guantes'].append(papa['idx_guantes'][0])
            jugador1['idx_pecheras'].append(mama['idx_pecheras'][0])
            jugador2['idx_pecheras'].append(papa['idx_pecheras'][0])
        if locus == 3:
            jugador1['altura'].append(papa['altura'][0])
            jugador2['altura'].append(mama['altura'][0])
            jugador1['idx_armas'].append(papa['idx_armas'][0])
            jugador2['idx_armas'].append(mama['idx_armas'][0])
            jugador1['idx_botas'].append(papa['idx_botas'][0])
            jugador2['idx_botas'].append(mama['idx_botas'][0])
            jugador1['idx_cascos'].append(mama['idx_cascos'][0])
            jugador2['idx_cascos'].append(papa['idx_cascos'][0])
            jugador1['idx_guantes'].append(mama['idx_guantes'][0])
            jugador2['idx_guantes'].append(papa['idx_guantes'][0])
            jugador1['idx_pecheras'].append(mama['idx_pecheras'][0])
            jugador2['idx_pecheras'].append(papa['idx_pecheras'][0])
        if locus == 4:
            jugador1['altura'].append(papa['altura'][0])
            jugador2['altura'].append(mama['altura'][0])
            jugador1['idx_armas'].append(papa['idx_armas'][0])
            jugador2['idx_armas'].append(mama['idx_armas'][0])
            jugador1['idx_botas'].append(papa['idx_botas'][0])
            jugador2['idx_botas'].append(mama['idx_botas'][0])
            jugador1['idx_cascos'].append(papa['idx_cascos'][0])
            jugador2['idx_cascos'].append(mama['idx_cascos'][0])
            jugador1['idx_guantes'].append(mama['idx_guantes'][0])
            jugador2['idx_guantes'].append(papa['idx_guantes'][0])
            jugador1['idx_pecheras'].append(mama['idx_pecheras'][0])
            jugador2['idx_pecheras'].append(papa['idx_pecheras'][0])
        if locus == 5:
            jugador1['altura'].append(papa['altura'][0])
            jugador2['altura'].append(mama['altura'][0])
            jugador1['idx_armas'].append(papa['idx_armas'][0])
            jugador2['idx_armas'].append(mama['idx_armas'][0])
            jugador1['idx_botas'].append(papa['idx_botas'][0])
            jugador2['idx_botas'].append(mama['idx_botas'][0])
            jugador1['idx_cascos'].append(papa['idx_cascos'][0])
            jugador2['idx_cascos'].append(mama['idx_cascos'][0])
            jugador1['idx_guantes'].append(papa['idx_guantes'][0])
            jugador2['idx_guantes'].append(mama['idx_guantes'][0])
            jugador1['idx_pecheras'].append(mama['idx_pecheras'][0])
            jugador2['idx_pecheras'].append(papa['idx_pecheras'][0])
        if locus == 6:
            jugador1['altura'].append(papa['altura'][0])
            jugador2['altura'].append(mama['altura'][0])
            jugador1['idx_armas'].append(papa['idx_armas'][0])
            jugador2['idx_armas'].append(mama['idx_armas'][0])
            jugador1['idx_botas'].append(papa['idx_botas'][0])
            jugador2['idx_botas'].append(mama['idx_botas'][0])
            jugador1['idx_cascos'].append(papa['idx_cascos'][0])
            jugador2['idx_cascos'].append(mama['idx_cascos'][0])
            jugador1['idx_guantes'].append(papa['idx_guantes'][0])
            jugador2['idx_guantes'].append(mama['idx_guantes'][0])
            jugador1['idx_pecheras'].append(papa['idx_pecheras'][0])
            jugador2['idx_pecheras'].append(mama['idx_pecheras'][0])

 
        nuevos_hijos.append(jugador1)
        nuevos_hijos.append(jugador2)

    #no calculo el desempenio, ni pi ni qi ya que aun tengo que mutar

    return nuevos_hijos

def cruza (met_cruza, padres,armas, botas, cascos, guantes, pecheras):
# 2 PUNTOS
# ANULAR
# UNIFORME
    nuevos_hijos = [] 
  
    np.random.shuffle(padres)
  
    if met_cruza == '1 punto':
        nuevos_hijos = un_punto(padres,armas, botas, cascos, guantes, pecheras)

    return nuevos_hijos

