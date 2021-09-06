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
# para los graficos
import time
# para el corte por tiempo
from datetime import datetime

# funciones mias
import calculos 
import seleccion_padres
import met_cruza
import met_mut
import implementacion
import corte
import graficos

#variables globales
armas=[]
botas=[]
cascos=[]
guantes=[]
pecheras=[]


#TO DO a lo ultimo cargar los archivos originales
def cargo_equipo():
    with open("allitems/armas.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        es_titulo = 1
        for line in tsv_file:
            if (es_titulo):
                es_titulo = 0
                continue
            armas.append(line)
        
    with open("allitems/botas.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        es_titulo = 1
        for line in tsv_file:
            if (es_titulo):
                es_titulo = 0
                continue
            botas.append(line)
    
    with open("allitems/cascos.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        es_titulo = 1
        for line in tsv_file:
            if (es_titulo):
                es_titulo = 0
                continue
            cascos.append(line)

    with open("allitems/guantes.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        es_titulo = 1
        for line in tsv_file:
            if (es_titulo):
                es_titulo = 0
                continue
            guantes.append(line)
            
    with open("allitems/pecheras.tsv") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        es_titulo = 1
        for line in tsv_file:
            if (es_titulo):
                es_titulo = 0
                continue
            pecheras.append(line)


# #######################################################################
# MAIN
# #######################################################################
empiezo = datetime.now()
poblacion = []
cargo_equipo()

#Abro el archivo de configuracion
f = open('config.json',)
data = json.load(f)

for i in data['TP1']:
    #recibo_clase (INPUT CLASE)
    clase = i['clase']
    #N    
    cant_pob = int(i['cantidad poblacion'])
    #K
    cant_ite = int(i['cantidad de individuos por iteración'])
    porc_padres = float(i['variable padres'])
    met_padres1 = i['metodo padres 1']
    met_padres2 = i['metodo padres 2']
    metodo_cruza = i ['metodo cruza']

    metodo_mutacion = i['metodo mutacion']
    Pm = float(i['mutacion Pm'])
    M = int(i['mutacion M'])

    porc_reemplazo = float(i['variable reemplazo'])
    met_reemplazo1 = i['metodo reemplazo 1']
    met_reemplazo2 = i['metodo reemplazo 2']
    met_implementacion = i['implementacion']

    tipo_corte = i['corte']
    var_corte = i['variable corte']
    var_corte_2 = i['otra variable corte']
    
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
        fuerza, agilidad, pericia, resistencia, vida = calculos.calculo_items(idx_armas, 
                                                                     idx_botas, 
                                                                     idx_cascos, 
                                                                     idx_guantes, 
                                                                     idx_pecheras,                  armas, botas, cascos, guantes, pecheras)
        ataque = (agilidad + pericia) * fuerza * atm
        defensa = (resistencia + pericia) * vida * dem
        desempenio = calculos.calculo_desempenio (clase, ataque, defensa)
        
        # print(clase, altura, atm, dem, idx_armas, idx_botas, idx_cascos, idx_guantes, idx_pecheras)    
        # print(fuerza, agilidad, pericia, resistencia, vida, ataque, defensa, desempenio)
        
        jugador = {'clase': [], 'altura': [], 'desempenio': [], 
                  'pi': [], 'qi': [],
                   'idx_armas': [], 'idx_botas': [],
                   'idx_cascos': [], 'idx_guantes': [],
                   'idx_pecheras': []}
        jugador['clase'].append(clase)
        jugador['altura'].append(altura)
        jugador['desempenio'].append(desempenio) 
        jugador['idx_armas'].append(idx_armas)
        jugador['idx_botas'].append(idx_botas)
        jugador['idx_cascos'].append(idx_cascos)
        jugador['idx_guantes'].append(idx_guantes)
        jugador['idx_pecheras'].append(idx_pecheras)
        poblacion.append(jugador)
    
f.close()

ronda = 1
#para trabajar corte por el mejor
una_lista = []
#para trabajar corte por la poblacion entera
toda_la_lista = []

plotter = graficos.Plotter(500,0,50)
minimo, promedio = calculos.guardar(ronda, poblacion)
time.sleep(.01)
plotter.plotdata( [minimo, minimo, promedio, promedio])


while(True):
    #  genero_padres (INPUT VARIABLE A)
    padres = []
    padres = seleccion_padres.elijo_padres(poblacion, porc_padres, cant_pob, cant_ite, met_padres1, met_padres2)
    
    # genero_cruza
    nuevos_hijos = []
    nuevos_hijos = met_cruza.cruza(metodo_cruza, padres, armas, botas, cascos, guantes, pecheras)
    
    # genero_mutacion
    nuevos_hijos = met_mut.mutacion(metodo_mutacion, nuevos_hijos, armas, botas, cascos, guantes, pecheras, Pm, M)
    
    # genero implementacion y reemplazo
    poblacion2 = []
    poblacion2 = implementacion.seleccion_poblacion(poblacion, nuevos_hijos, porc_reemplazo, cant_pob, cant_ite, met_reemplazo1, met_reemplazo2, met_implementacion)
    
    #guardo fitness promedio, minimo y la ronda
    
    minimo, promedio = calculos.guardar(ronda, poblacion2)
    time.sleep(.01)
    plotter.plotdata( [minimo, minimo, promedio, promedio])

    el_mejor = corte.devuelvo_mejor (poblacion2)
    #print('el mejor de esa poblacion', el_mejor)

    una_lista.insert(0,el_mejor)
    toda_la_lista.insert(0,poblacion2)
    
    if corte.se_corta(poblacion2, tipo_corte, var_corte, ronda, empiezo, promedio, una_lista, toda_la_lista, var_corte_2):
        poblacion =[]
        poblacion = poblacion2
        break
    else:
        poblacion =[]
        poblacion = poblacion2
        ronda = ronda + 1
    

input("Press Enter to continue...")

# devolver_mejor_personaje
el_mejor = corte.devuelvo_mejor (poblacion)
print(el_mejor)
termino = datetime.now()
# print('Tiempo total desde ', empiezo, ' y termino ', termino )
# print((termino - empiezo).total_seconds())


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
