# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 20:57:51 2021

@author: marce
"""

def se_corta(poblacion2, tipo_corte, var_corte, ronda):

    if (tipo_corte == 'cantidad generaciones'):
        var_corte = int(var_corte)
        if( var_corte == ronda):
            return True

    return False


def devuelvo_mejor (poblacion):
    
    list_desempenio = []
    for i in poblacion:
        list_desempenio.append(i['desempenio'])     
    elite = sorted(list_desempenio,reverse=True)
    el_mejor = elite[0][0]
    return (next((sub for sub in poblacion if sum(sub['desempenio']) == el_mejor), None))
