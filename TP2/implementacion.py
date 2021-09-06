# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 20:42:22 2021

@author: marce
"""

import seleccion_padres

# implementacion
# fill all
# a la poblacion y a los nuevos_hijos los uno
# y les aplico un metodo de seleccion
#     genero_reemplazo (INPUT VARIABLE B)
# fill parent usa N y K y de acuerdo a ellos, elije la nueva pob

    #N    
#    cant_pob = int(i['cantidad poblacion'])
    #K
#    cant_ite = int(i['cantidad de individuos por iteración'])

def seleccion_poblacion(poblacion, nuevos_hijos, porc_reemplazo, cant_pob, cant_ite, met_reemplazo1, met_reemplazo2, met_implementacion):

    if met_implementacion == 'fill-all':
        new_pob = poblacion + nuevos_hijos
    else:
        #fill-parent
        if cant_ite > cant_pob:
            new_pob = nuevos_hijos[:cant_pob]
        else:
            x = cant_pob - cant_ite
            new_pob = nuevos_hijos + poblacion[:x]
            
       
    return seleccion_padres.elijo_padres(new_pob, porc_reemplazo, cant_pob, cant_ite, met_reemplazo1, met_reemplazo2)

