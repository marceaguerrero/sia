# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 20:57:51 2021

@author: marce
"""
# para el corte por tiempo
from datetime import datetime

def se_corta(poblacion2, tipo_corte, var_corte, ronda, empiezo, prom_desempenio, una_lista, todas_poblaciones , var_corte_2):

    if (tipo_corte == 'cantidad generaciones'):
        var_corte = int(var_corte)
        if( var_corte == ronda):
            return True

    if (tipo_corte == 'tiempo'):
        termino = datetime.now()
        total = (termino - empiezo).total_seconds()
        if total >= float(var_corte):
            return True

    if (tipo_corte == 'fitness objetivo'):
        var_corte = int(var_corte)
        if prom_desempenio >= float(var_corte):
            return True
        
    if (tipo_corte == 'estructura'):      
        #este parametro me dice cuantas generaciones
        var_corte = int(var_corte)
        cant_generaciones = 0
        if(len(todas_poblaciones) <= var_corte ):
            #print('salgo porque aun no cuento con suficientes poblaciones')
            return False
        
        #este parametro me dice el porcentaje de jugadores similares
               
#todas_poblaciones = [{'id':'1234','name':'Jason'}, {'id':'2345','name':'Tom'}, {'id':'3456','name':'Art'}]
        #print(todas_poblaciones)
        while (todas_poblaciones):
            primer_poblacion = todas_poblaciones.pop()
            var_corte_2 = float(var_corte_2)            
            cant_porc = int (var_corte_2 * len(primer_poblacion))
            cant_buscados = 0
            # print('busco ', cant_porc, cant_buscados)
            #print('busco en ', primer_poblacion)

            #aca es adonde busco, en la poblacion inmediatamente siguiente
            segunda_poblacion = todas_poblaciones.pop()
            todas_poblaciones.insert(0, segunda_poblacion)
            
            for jugador in primer_poblacion:
                #print('mi primer jugador ', jugador)
                # cuantos jugadores similares tengo qeu encontrar
                #agarro un jugador
                altura = jugador['altura']
                desempenio = jugador['desempenio']              
                tom_index = -1
                tom_index = next((index for (index, d) in enumerate(segunda_poblacion) if (d['desempenio'] == desempenio and d['altura'] == altura)), None)
                if (tom_index):
                    if cant_buscados == cant_porc:
                        if cant_generaciones == var_corte:
                            #print('Fin')
                            return True
                        else:
                            cant_generaciones = cant_generaciones + 1
                    else:
                        cant_buscados = cant_buscados + 1
            
            #termine la poblacion
            if cant_buscados != cant_porc:
                #print ('termine la poblacion pero no encontre lo que buscaba')
                return False
            #sino quiere decir que me faltan generaciones, vuelvo a empezar

        
    if (tipo_corte == 'contenido'):
        var_corte = int(var_corte)
        if(len(una_lista) <= var_corte ):
            #print('salgo porque aun no cuento con suficientes jugadores')
            return False
        
        lis_desempenio = una_lista
        #cantidad de generaciones
        #busco en la lista de contenidos, si para esas generaciones el desempenio es igual
        aux = 0
        ronda = 1
        desem = 0 
        for i in lis_desempenio:
            #print('val : ', aux, desem, ronda, i)
            if ronda == 1:
                aux =  i['desempenio'][0]
                ronda = ronda + 1
            else:
                desem = i['desempenio'][0]
                # si el desempenio se mantiene y la ronda es igual al parametro
                if (aux != desem):
                    #print('sali por false en ronda', ronda)
                    return False
                if (aux == desem and ronda == var_corte):                   
                    #print('sali por true')
                    return True
                if (aux == desem and ronda < var_corte):
                    ronda = ronda + 1
                    aux = desem
                else :
                    aux = desem

    # print('sali por false')
    return False


def devuelvo_mejor (poblacion):
    
    list_desempenio = []
    for i in poblacion:
        list_desempenio.append(i['desempenio'])     
    elite = sorted(list_desempenio,reverse=True)
    el_mejor = elite[0][0]
    return (next((sub for sub in poblacion if sum(sub['desempenio']) == el_mejor), None))
