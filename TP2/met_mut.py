# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:20:00 2021

@author: marce
"""
import random
import seleccion_padres
import calculos

def mut_gen (nuevos_hijos, armas, botas, cascos, guantes, pecheras):

    #solo muta 1 gen - random cual
    que_gen = int(random.uniform(0, 5))
    pos = 0
    for i in nuevos_hijos:
        #cada hijo
        #si es altura
        pm = random.uniform(0.25, 1)
        if pm >= 0.5:
            if que_gen == 0:
                #1.3y 2
                altura = random.uniform(1.3, 2.)
                nuevos_hijos[pos]['altura'].clear()        
                nuevos_hijos[pos]['altura'].append(altura)
            #en el caso de las herramientas           
            elif que_gen == 1:          
                idx = int(random.uniform(0, 999999))
                nuevos_hijos[pos]['idx_armas'].clear()        
                nuevos_hijos[pos]['idx_armas'].append(idx)
            elif que_gen == 2:          
                idx = int(random.uniform(0, 999999))
                nuevos_hijos[pos]['idx_botas'].clear()        
                nuevos_hijos[pos]['idx_botas'].append(idx)
            elif que_gen == 3:          
                idx = int(random.uniform(0, 999999))
                nuevos_hijos[pos]['idx_cascos'].clear()        
                nuevos_hijos[pos]['idx_cascos'].append(idx)
            elif que_gen == 4:          
                idx = int(random.uniform(0, 999999))
                nuevos_hijos[pos]['idx_guantes'].clear()        
                nuevos_hijos[pos]['idx_guantes'].append(idx)
            elif que_gen == 5:          
                idx = int(random.uniform(0, 999999))
                nuevos_hijos[pos]['idx_pecheras'].clear()        
                nuevos_hijos[pos]['idx_pecheras'].append(idx)

 
        #desempenio del hijo
        atm = 0.7 - ((float(nuevos_hijos[pos]['altura'][0])*3)-5)**4 + ((float(nuevos_hijos[pos]['altura'][0])*3)-5)**2 + (float(nuevos_hijos[pos]['altura'][0])/4)
        dem = 1.9 + ((float(nuevos_hijos[pos]['altura'][0])*2.5) - 4.16)**4 - ((float(nuevos_hijos[pos]['altura'][0])*2.5) - 4.16)**2 - ((float(nuevos_hijos[pos]['altura'][0])*3)/10)
        fuerza, agilidad, pericia, resistencia, vida = calculos.calculo_items(nuevos_hijos[pos]['idx_armas'][0], 
                                                                      nuevos_hijos[pos]['idx_botas'][0], 
                                                                      nuevos_hijos[pos]['idx_cascos'][0], 
                                                                      nuevos_hijos[pos]['idx_guantes'][0],                                                                       
                                                                    nuevos_hijos[pos]['idx_pecheras'][0], armas, botas, cascos, guantes, pecheras)
        ataque = (agilidad + pericia) * fuerza * atm
        defensa = (resistencia + pericia) * vida * dem
        desempenio = calculos.calculo_desempenio (nuevos_hijos[pos]['clase'][0], ataque, defensa)        
        nuevos_hijos[pos]['desempenio'].append(desempenio)

        pos = pos + 1
    
    return nuevos_hijos

def mutacion(metodo_mutacion, nuevos_hijos, armas, botas, cascos, guantes, pecheras):
  
    nuevos_hijos = mut_gen (nuevos_hijos, armas, botas, cascos, guantes, pecheras)

    nuevos_hijos = seleccion_padres.calculo_pi(nuevos_hijos)
    
    return nuevos_hijos
