# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 00:30:14 2021

@author: marce
"""

import random
import struct 
import TP2
import seleccion_padres

def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def un_punto(padres):
    
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

        jugador = {'clase': [], 'altura': [], 'desempenio': [], 
                  'pi': [], 'qi': [],
                   'idx_armas': [], 'idx_botas': [],
                   'idx_cascos': [], 'idx_guantes': [],
                   'idx_pecheras': []}
        
        jugador['clase'].append(papa['clase'])
        
        prom_altura = TP2.bin_to_float(altura)
        atm = 0.7 - ((prom_altura*3)-5)**4 + ((prom_altura*3)-5)**2 + (prom_altura/4)
        dem = 1.9 + ((prom_altura*2.5) - 4.16)**4 - ((prom_altura*2.5) - 4.16)**2 - ((prom_altura*3)/10)
        #genero_desempeño
        fuerza, agilidad, pericia, resistencia, vida = TP2.calculo_items(idx_armas, 
                                                                     idx_botas, 
                                                                     idx_cascos, 
                                                                     idx_guantes, 
                                                                     idx_pecheras)
        ataque = (agilidad + pericia) * fuerza * atm
        defensa = (resistencia + pericia) * vida * dem
        desempenio = TP2.calculo_desempenio (papa['clase'], ataque, defensa)

        jugador['desempenio'].append(desempenio) 
        jugador['idx_armas'].append(TP2.float_to_bin(idx_armas))
        jugador['idx_botas'].append(TP2.float_to_bin(idx_botas))
        jugador['idx_cascos'].append(TP2.float_to_bin(idx_cascos))
        jugador['idx_guantes'].append(TP2.float_to_bin(idx_guantes))
        jugador['idx_pecheras'].append(TP2.float_to_bin(idx_pecheras))


        nuevos_hijos.append(jugador)

    nuevos_hijos = seleccion_padres.calculo_pi(nuevos_hijos)

    return nuevos_hijos

def cruza (met_cruza, padres):
# 1 PUNTO
# 2 PUNTOS
# ANULAR
# UNIFORME
    nuevos_hijos = [] 
    if met_cruza == '1 punto':
        un_punto(padres)
        
    return nuevos_hijos

