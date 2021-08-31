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
# fill parent ver explicacion


def seleccion_poblacion(poblacion, nuevos_hijos, porc_reemplazo, cant_pob, cant_ite, met_reemplazo1, met_reemplazo2, met_implementacion):

    if met_implementacion == 'fill-all':
        new_pob = poblacion + nuevos_hijos
        return seleccion_padres.elijo_padres(new_pob, porc_reemplazo, cant_pob, cant_ite, met_reemplazo1, met_reemplazo2)
       
        
    else: #fill parent TO DO
        return 0
    
    return 0

