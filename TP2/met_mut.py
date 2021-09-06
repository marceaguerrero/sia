# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:20:00 2021

@author: marce
"""
import random
import seleccion_padres
import calculos

def mut_gen (nuevos_hijos, armas, botas, cascos, guantes, pecheras, Pm):
    
    #solo muta 1 gen - random cual
    que_gen = int(random.uniform(0, 5))
    pos = 0
    x = int(Pm * len( nuevos_hijos))
    for i in nuevos_hijos:

        if (x > 0 ):
            x = x - 1
            #si es altura
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

def mut_multigen_lim (nuevos_hijos, armas, botas, cascos, guantes, pecheras, Pm, M):
       
    #muta M genes que es parámetro
    pos = 0
    x = int(Pm * len( nuevos_hijos))
    for i in nuevos_hijos:

        if (x > 0 ):
            x = x - 1
            #si es altura
            if M >=1:
                #1.3y 2
                altura = random.uniform(1.3, 2.)
                nuevos_hijos[pos]['altura'].clear()        
                nuevos_hijos[pos]['altura'].append(altura)
            #en el caso de las herramientas           
            if M >=2:
                idx = int(random.uniform(0, 999999))
                nuevos_hijos[pos]['idx_armas'].clear()        
                nuevos_hijos[pos]['idx_armas'].append(idx)
            if M >=3:
                idx = int(random.uniform(0, 999999))
                nuevos_hijos[pos]['idx_botas'].clear()        
                nuevos_hijos[pos]['idx_botas'].append(idx)
            if M >=4:
                idx = int(random.uniform(0, 999999))
                nuevos_hijos[pos]['idx_cascos'].clear()        
                nuevos_hijos[pos]['idx_cascos'].append(idx)
            if M >=5:
                idx = int(random.uniform(0, 999999))
                nuevos_hijos[pos]['idx_guantes'].clear()        
                nuevos_hijos[pos]['idx_guantes'].append(idx)
            if M >=6:
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

def mut_multigen_unif (nuevos_hijos, armas, botas, cascos, guantes, pecheras, Pm, M):
     
    #cada gen tiene una probabilidad Pm de ser mutado
    pos = 0
    x = int(Pm * len( nuevos_hijos))
    x_altura = x
    x_armas = x
    x_botas = x
    x_cascos = x
    x_guantes = x
    x_pecheras = x 
    for i in nuevos_hijos:

        if (x_altura > 0 ):
            x_altura = x_altura - 1
            altura = random.uniform(1.3, 2.)
            nuevos_hijos[pos]['altura'].clear()        
            nuevos_hijos[pos]['altura'].append(altura)
        
        if (x_armas> 0 ):
            x_armas= x_armas- 1
            idx = int(random.uniform(0, 999999))
            nuevos_hijos[pos]['idx_armas'].clear()        
            nuevos_hijos[pos]['idx_armas'].append(idx)

        if (x_botas> 0 ):
            x_botas= x_botas- 1
            idx = int(random.uniform(0, 999999))
            nuevos_hijos[pos]['idx_botas'].clear()        
            nuevos_hijos[pos]['idx_botas'].append(idx)

        if (x_cascos> 0 ):
            x_cascos= x_cascos- 1
            idx = int(random.uniform(0, 999999))
            nuevos_hijos[pos]['idx_cascos'].clear()        
            nuevos_hijos[pos]['idx_cascos'].append(idx)

        if (x_guantes> 0 ):
            x_guantes= x_guantes- 1
            idx = int(random.uniform(0, 999999))
            nuevos_hijos[pos]['idx_guantes'].clear()        
            nuevos_hijos[pos]['idx_guantes'].append(idx)

        if (x_pecheras> 0 ):
            x_pecheras= x_pecheras- 1
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

def mut_completa (nuevos_hijos, armas, botas, cascos, guantes, pecheras, Pm, M):
     
    #todos los genes cambian con probabilidad Pm 
    pos = 0
    x = int(Pm * len( nuevos_hijos))
    for i in nuevos_hijos:

        if (x > 0 ):
            x = x - 1
            altura = random.uniform(1.3, 2.)
            nuevos_hijos[pos]['altura'].clear()        
            nuevos_hijos[pos]['altura'].append(altura)
            idx = int(random.uniform(0, 999999))
            nuevos_hijos[pos]['idx_armas'].clear()        
            nuevos_hijos[pos]['idx_armas'].append(idx)
            idx = int(random.uniform(0, 999999))
            nuevos_hijos[pos]['idx_botas'].clear()        
            nuevos_hijos[pos]['idx_botas'].append(idx)
            idx = int(random.uniform(0, 999999))
            nuevos_hijos[pos]['idx_cascos'].clear()        
            nuevos_hijos[pos]['idx_cascos'].append(idx)
            idx = int(random.uniform(0, 999999))
            nuevos_hijos[pos]['idx_guantes'].clear()        
            nuevos_hijos[pos]['idx_guantes'].append(idx)
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

def mutacion(metodo_mutacion, nuevos_hijos, armas, botas, cascos, guantes, pecheras, Pm, M):
  
    if metodo_mutacion == 'gen':
        nuevos_hijos = mut_gen (nuevos_hijos, armas, botas, cascos, guantes, pecheras, Pm)
    elif metodo_mutacion == 'multigen limitada':
        nuevos_hijos = mut_multigen_lim (nuevos_hijos, armas, botas, cascos, guantes, pecheras, Pm, M)
    elif metodo_mutacion == 'multigen uniforme':
        nuevos_hijos = mut_multigen_unif (nuevos_hijos, armas, botas, cascos, guantes, pecheras, Pm, M)
    elif metodo_mutacion == 'completa':
        nuevos_hijos = mut_completa (nuevos_hijos, armas, botas, cascos, guantes, pecheras, Pm, M)

    nuevos_hijos = seleccion_padres.calculo_pi(nuevos_hijos)
    
    return nuevos_hijos
