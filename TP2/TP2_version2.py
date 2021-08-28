# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 19:05:48 2021

@author: marce
"""
# para leer el dataset
import csv
# para leer el archivo de configuracion
import json
# para generar la altura
import random
# para la tangente hiperbolica
import math
# para convertir a bits
import struct


#variables globales
armas=[]
botas=[]
cascos=[]
guantes=[]
pecheras=[]


def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]


#TO DO a lo ultimo cargar los archivos originales
def cargo_equipo():
    with open("allitems/armas_recorte.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        es_titulo = 1
        for line in tsv_file:
            if (es_titulo):
                es_titulo = 0
                continue
            armas.append(line)
        
    with open("allitems/botas_recorte.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        es_titulo = 1
        for line in tsv_file:
            if (es_titulo):
                es_titulo = 0
                continue
            botas.append(line)
    
    with open("allitems/cascos_recorte.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        es_titulo = 1
        for line in tsv_file:
            if (es_titulo):
                es_titulo = 0
                continue
            cascos.append(line)

    with open("allitems/guantes_recorte.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        es_titulo = 1
        for line in tsv_file:
            if (es_titulo):
                es_titulo = 0
                continue
            guantes.append(line)
            
    with open("allitems/pecheras_recorte.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        es_titulo = 1
        for line in tsv_file:
            if (es_titulo):
                es_titulo = 0
                continue
            pecheras.append(line)


def calculo_items(idx_armas, idx_botas, idx_cascos, idx_guantes, idx_pecheras):
    
    #id	Fu	Ag	Ex	Re	Vi
    fuerza_total = 0    
    fuerza = 0
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
    
    if (clase == 'guerrero'):
        return (0.6 * ataque) + (0.6 * defensa)

    if (clase == 'arquero'):
        return (0.9 * ataque) + (0.1 * defensa)
    
    if (clase == 'defensor'):
        return (0.3 * ataque) + (0.8 * defensa)

    if (clase == 'infiltrado'):
        return (0.8 * ataque) + (0.3 * defensa)

    return desempenio

def calculo_pi(jugador):
    
    sum_total = sum(jugador['desempenio'])
    pi = 0
    sum_pi = 0 
    for i in jugador['desempenio']:
        pi = i / sum_total
        sum_pi = sum_pi + pi
        jugador['pi'].append( pi)
        jugador['qi'].append(sum_pi )
    return jugador

def seleccion_elite (porcentaje, cant_pob, jugador):

    #cantidad a seleccionar por ejemplo 0,4 * 100
    K = int(porcentaje * cant_pob)
    #tengo que ordenar y obtener los K con mejor valor
    elite = sorted(jugador['desempenio'],reverse=True)
    
    print(elite)
    
    return elite[:K]

def seleccion_ruleta (porcentaje, cant_pob, jugador):

    #cantidad a seleccionar por ejemplo 0,4 * 100
    K = int(porcentaje * cant_pob)
    ruleta = []

    #genero K numeros al azar

    for i in range(K):
        nro = random.uniform(0, 1)
        aux = 0 
        for i in jugador['qi']:
            if i < nro:
                aux = i
            else:
                ruleta.append(i)
                break
    
    #busco en qi esos numeros y listo bye bye
    print(ruleta)
    return ruleta

def seleccion_padres(jugador, porcentaje, cant_pob, met_padres1, met_padres2):
 # Universal
 # Boltzmann
 # Torneos (ambas versiones)
 # Ranking
 
    #Necesito las frecuencias relativas y acumuladas
    jugador = calculo_pi(jugador)
    
    padres = []

    if met_padres1 == 'elite':
        padres = seleccion_elite (porcentaje, cant_pob, jugador)

    if met_padres1 == 'ruleta':
        padres = seleccion_ruleta (porcentaje, cant_pob, jugador)

    if met_padres2 == 'elite':
        padres.extend(seleccion_elite (1 - porcentaje, cant_pob, jugador))

    if met_padres2 == 'ruleta':
        padres = seleccion_ruleta (1 - porcentaje, cant_pob, jugador)

    return padres
    
# #######################################################################
# MAIN
# #######################################################################

jugador = {'clase': [], 'altura': [], 'desempenio': [], 
          'pi': [], 'qi': [],
           'idx_armas': [], 'idx_botas': [],
           'idx_cascos': [], 'idx_guantes': [],
           'idx_pecheras': []}
cargo_equipo()

#Abro el archivo de configuracion
f = open('config.json',)
data = json.load(f)
  
for i in data['TP1']:
    #recibo_clase (INPUT CLASE)
    clase = i['clase']
    cant_pob = int(i['cantidad poblacion'])
    porc_padres = float(i['variable padres'])
    met_padres1 = i['metodo padres 1']
    met_padres2 = i['metodo padres 2']

    for z in range(cant_pob):
        #genero_altura
        altura = random.uniform(1.3, 2.)
        atm = 0.7 - ((altura*3)-5)**4 + ((altura*3)-5)**2 + (altura/4)
        dem = 1.9 + ((altura*2.5) - 4.16)**4 - ((altura*2.5) - 4.16)**2 - ((altura*3)/10)
        
        #tomo_1_equipo de cada uno
        idx_armas = random.randint(0,len(armas)-1)
        idx_botas = random.randint(0,len(botas)-1)
        idx_cascos = random.randint(0,len(cascos)-1)
        idx_guantes = random.randint(0,len(guantes)-1)
        idx_pecheras = random.randint(0,len(pecheras)-1)
        
        #genero_desempeño
        fuerza, agilidad, pericia, resistencia, vida = calculo_items(idx_armas, 
                                                                     idx_botas, 
                                                                     idx_cascos, 
                                                                     idx_guantes, 
                                                                     idx_pecheras)
        ataque = (agilidad + pericia) * fuerza * atm
        defensa = (resistencia + pericia) * vida * dem
        desempenio = calculo_desempenio (clase, ataque, defensa)
        
        # print(clase, altura, atm, dem, idx_armas, idx_botas, idx_cascos, idx_guantes, idx_pecheras)    
        # print(fuerza, agilidad, pericia, resistencia, vida, ataque, defensa, desempenio)
        
        jugador['clase'].append(clase)
        jugador['altura'].append(float_to_bin(altura))
        jugador['desempenio'].append(desempenio) 
        jugador['idx_armas'].append(float_to_bin(idx_armas))
        jugador['idx_botas'].append(float_to_bin(idx_botas))
        jugador['idx_cascos'].append(float_to_bin(idx_cascos))
        jugador['idx_guantes'].append(float_to_bin(idx_guantes))
        jugador['idx_pecheras'].append(float_to_bin(idx_pecheras))


#print(jugador)
f.close()


# mientras condicion de corte
#     genero_padres (INPUT VARIABLE A)

 # Elite : los que tienen mayor aptitud
padres = []
padres = seleccion_padres(jugador, porc_padres, cant_pob, met_padres1, met_padres2)
print(padres)
print(jugador)

#     genero_cruza
#     genero_mutacion
#     genero_reemplazo (INPUT VARIABLE B)

# devolver_mejor_personaje






# #######################################################################
# PSEUDO CODIGO
# #######################################################################
#cargo_equipo

# mientras haya entrada
#     recibo_clase (INPUT CLASE)
#     genero_altura
#     tomo_1_equipo
#     genero_desempeño
#     agrego_jugador
#     genero_poblacion_para_esa_configuracion

# ya tengo mi poblacion

# mientras condicion de corte
#     genero_padres (INPUT VARIABLE A)
#     genero_cruza
#     genero_mutacion
#     genero_reemplazo (INPUT VARIABLE B)

# devolver_mejor_personaje

# #######################################################################
# DUDAS
# #######################################################################
# yo recibo una configuracion para un guerrero y un arquero 
    #y voy generando varios de esos para armar la primer poblacion. Cuantos genero?
    #sobre todos los que son guerreros voy generando padres, cruzas, mutaciones y reemplazos
    # o es sobre toda la poblacion que hago eso?
    
# como se configura el gen del jugador? yo pense en usar el desempeño
# como se cual es la mejor configuración o el fitness mínimo (objetivo)?
# cual es la diferencia de corte por estructura y por fitness objetivo?
