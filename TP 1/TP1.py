# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:14:54 2021

@author: marce
"""
import time
import math

#matriz donde guardo el juego
data = []
#estado inicial 
paredes_ubicacion = list()
jugador_x = 0
jugador_y = 0
cajas_ubicacion = list()
objetivos_ubicacion = list()
deadlock_ubicacion = list()
col_max = 0
fil_max = 0

def estan_alineados(jugador_x, jugador_y, caja_x, caja_y, dir_x, dir_y):

    #vamos para arriba
    if (jugador_x == caja_x + 1 and caja_x == dir_x + 1 and jugador_y == caja_y and caja_y == dir_y):
        return True
    #vamos para abajo
    elif (jugador_x + 1== caja_x and caja_x + 1== dir_x  and jugador_y == caja_y and caja_y == dir_y):
        return True
    #vamos a la izquierda
    elif (jugador_x == caja_x and caja_x == dir_x  and jugador_y == caja_y + 1 and caja_y == dir_y + 1):
        return True
    #vamos a la derecha
    elif (jugador_x == caja_x and caja_x == dir_x  and jugador_y + 1== caja_y  and caja_y + 1== dir_y ):
        return True
    
    return False


def puede_llegar(suc_x, suc_y, voy_x, voy_y, fil_max, col_max):
    #en los espacios que tengo para moverme no tengo posibilidad de llegar al objetivo
    #tengo que probar con todos los sucesores en nivel 1 a ver que camino me conviene
    #print('entro en puede_llegar')
    if (suc_x==voy_x and suc_y==voy_y):
        return True

    nodo = (suc_x, suc_y)
    visited = [] #Nodos visitados
    Fr = [] #Conjunto frontera
    Fr.append(nodo)
    visited.append(nodo)
    exito = 0
    while(Fr):
        n = Fr.pop()
        if (n[0] == voy_x and n[1]== voy_y):       
            return True
        sucesores = genero_hijos(n, fil_max, col_max)
        if sucesores:
            for aux_sucesor in sucesores:
                if aux_sucesor not in visited:
                    Fr.append(aux_sucesor)
                    visited.append(aux_sucesor)

    #print('vuelta sin exito de ', sssss, 'que va a ', voy_x, voy_y)
                
    return False


def voy_para_alla(pos_jugador_x, pos_jugador_y, voy_x, voy_y, fil_max, col_max):
#el jugador tiene que remarla para llegar a empujar la caja
#tiene que elegir lugares que no sean pared ni objetivo
    vueltas = 1
    costo = 0 
    visited_1 = list()
    visited_1.append((pos_jugador_x, pos_jugador_y))
    sucesores = []
    # print('entro en voy_para_alla')
    # print(pos_jugador_x , voy_x , pos_jugador_y , voy_y)
    while(pos_jugador_x != voy_x or pos_jugador_y != voy_y):
        #lo puse para controlar el while, volarlo
        vueltas = vueltas + 1
        if vueltas > 15:
            # print('me voy por cantidad de vueltas')
            return costo, pos_jugador_x, pos_jugador_y
            break

        # print(pos_jugador_x , voy_x , pos_jugador_y , voy_y)
        sucesores = genero_hijos((pos_jugador_x, pos_jugador_y), fil_max, col_max)
        # print('sucesores del problema son ', sucesores)
        if sucesores:
            # de los que no visité, cual tiene menor distancia manhatan
            dist_man = 100
            distance = 0
            suc_x = 0
            suc_y = 0
            for aux_sucesor in sucesores:
                if aux_sucesor not in visited_1:  
                    # print(aux_sucesor[0], aux_sucesor[1], voy_x, voy_y, fil_max, col_max)                        
                    if(puede_llegar(aux_sucesor[0], aux_sucesor[1], voy_x, voy_y, fil_max, col_max)):                        
                        # print('puede llegar')
                        distance = abs(voy_x - aux_sucesor[0]) + abs(voy_y - aux_sucesor[1])
                        if(distance < dist_man):
                            dist_man = distance
                            suc_x = aux_sucesor[0]
                            suc_y = aux_sucesor[1]
            
            aux_sucesor = (suc_x, suc_y)
            # print ('tomo ', aux_sucesor, 'cuya distancia fue ', dist_man)
            data[aux_sucesor[0]][aux_sucesor[1]]= '@'
            data[pos_jugador_x][pos_jugador_y]= ' '        
            pos_jugador_x = aux_sucesor[0]
            pos_jugador_y = aux_sucesor[1]
            # print('nuevo valro', pos_jugador_x, pos_jugador_y)
            imprimir_estado(data)
            visited_1.append(aux_sucesor)
            costo = costo + 1
            if(pos_jugador_x == voy_x and pos_jugador_y == voy_y):
                return costo, pos_jugador_x, pos_jugador_y
            else:
                continue

    return costo, pos_jugador_x, pos_jugador_y


def imprimir_estado(data):
    for i in data:
        linea = ''
        for z in i:
            linea = linea + z
        print(linea)

def es_deadlock(fila, col):
    if (data[fila][col]=="." or data[fila][col]=="#"):
        return False
    
    #tengo que controlar que no me voy de los rangos del juego
    if (data[fila-1][col] == '#' and 
        (data[fila][col-1] == '#'  or
        data[fila][col+1] == '#' )):
        return True
            
    if (data[fila+1][col] == '#' and 
         (data[fila][col+1] == '#' or
          data[fila][col-1] == '#' )):
         return True

    return False

def genero_estado_inicial(filename):
    i_fila = 0
    i_col = 0
    col_max = 0
    with open(filename, "r") as f_in:
        lines = f_in.readlines()
        for i in lines:
            result = list(i)
            del result[-1]
            data.append(result)
            for i in result:
                if i == '#':
                    paredes_ubicacion.append((i_fila, i_col))
                elif i == '@':
                    jugador_x = i_fila
                    jugador_y = i_col
                elif i == '$':
                    cajas_ubicacion.append((i_fila, i_col))
                elif i == '.':
                    objetivos_ubicacion.append((i_fila, i_col))                   
                   
                i_col = i_col + 1
            if col_max < i_col:
                col_max = i_col
                
            i_col = 0
            i_fila = i_fila + 1
 
    fil_max = i_fila 
    x = 0
    y = 0 
    #print(fil_max, col_max)
    for x in range(1, fil_max -1 ):
        for y in range(1, col_max -1): 
            if (data[x][y]):
                if es_deadlock(x, y):
                    deadlock_ubicacion.append((x, y))
    
    return (jugador_x, jugador_y), fil_max, col_max

def genero_nodo(valor):
    if (valor == '#'):
        return False
    if (valor == '@'):
        return False
    if (valor == '$'):
        return False
    return True

def genero_hijos(nodo, fil_max, col_max):
    jugador_x = nodo[0]
    jugador_y = nodo[1]
    hijo=[]
    #no es nodo si es pared
    #me puedo mover para derecha
    fil_max = fil_max - 1
    col_max = col_max - 1
    
    if(jugador_y+1<=col_max):
        if(genero_nodo(data[jugador_x][jugador_y+1])):
            if (not es_deadlock(jugador_x,jugador_y+1)):
                hijo.append((jugador_x,jugador_y+1))
    #me puedo mover para izquierda
    if(jugador_y-1>=0):
        if(genero_nodo(data[jugador_x][jugador_y-1])):
            if (not es_deadlock(jugador_x,jugador_y-1)):
                hijo.append((jugador_x,jugador_y-1))
    #me puedo mover para abajo
    if(jugador_x+1<=fil_max):
        if(genero_nodo(data[jugador_x+1][jugador_y])):
            if (not es_deadlock(jugador_x+1,jugador_y)):
                hijo.append((jugador_x+1,jugador_y))
    #me puedo mover para arriba
    if(jugador_x-1>=0):
        if(genero_nodo(data[jugador_x-1][jugador_y])):
            if (not es_deadlock(jugador_x-1,jugador_y)):
                hijo.append((jugador_x-1,jugador_y))

    return hijo

def imprimo_arbol(mi_arbol):
    pos = 0
    for value in mi_arbol:
        print(pos, value)
        pos = pos + 1

def nivel_en_arbol(mi_arbol, valor):
    pos = 0
    # print('busco', valor)
    # imprimo_arbol(mi_arbol)
    for value in mi_arbol:
        # print(value, pos)
        if(len(value)==1):
            zz = []
            zz.append(valor)
            if(zz == value):
                       # print('devuelvo 0 que es la raiz', zz)
                       return pos
        if pos == len(mi_arbol):
            return 0
        for m in value:
            for i in m:
                #print(i)
                if (i==valor):
                    # print('encontrado, goodbye', pos)
                    return pos
        pos = pos + 1
    return 0

def busco_camino(metodo, mi_arbol, Tr, n, fil_max, col_max):
    solucion = []
    
    if (metodo == 'bfs'):
        nivel = nivel_en_arbol(mi_arbol, n) 
        #print('busco ', n , 'cuyo nivel es ', nivel)
        #imprimo_arbol(mi_arbol)

        solucion = []
        solucion.append(n)
        while(nivel >1):
            nivel = nivel - 1
            #print('busco en nivel ', nivel, ' al padre de ', n)
            encontrado = 0
            for nodos in mi_arbol[nivel]:
                #print('posibles padres ', nodos)
                # if(len(nodos)==2):
                #     print('raiz')
                #     #llegue a la raiz
                #     break
                #     sucesores = genero_hijos(nodos, fil_max, col_max)
                #     for aux in sucesores:
                #         if (aux == n):
                #             solucion.append(nodos)
                #             n = nodos
                #else:                    
                for nodo in nodos:
                    sucesores = genero_hijos(nodo, fil_max, col_max)
                    #print('sucesores', sucesores, 'de ', nodo)
                    for aux in sucesores:
                        if (aux == n):
                            #print('alcohana ', aux, n )
                            encontrado = 1
                            solucion.append(nodo)
                            n = nodo
                            break
                    if encontrado == 1:                        
                        break
                if encontrado == 1:
                    encontrado = 0
                    break
        
    if (metodo == 'dfs' or metodo == 'ggs'):
        #el ultimo es el objetivo
        valor = Tr.pop()
        if (valor == n):
            solucion.append(valor)
        else:
            print('Houston tenemos un problema')
        #el siguiente me dice en que nivel del arbol estoy
        valor = Tr.pop()
        #porque ya tome los dos anteriores
        nivel_max = nivel_en_arbol(mi_arbol, valor) -1 
        solucion.append(valor)
        encontrado = 0
        adentro = 0
        while(Tr):
            valor = Tr.pop()

            if encontrado != 0:
                solucion.append(adentro)  
                encontrado = 0
                if nivel_max == 0:
                    break
                nivel_max = nivel_max - 1
            
            for value in mi_arbol[nivel_max]: 
                    for i in value:
                        if (i==valor):
                            adentro = valor
                            encontrado = 1
    return solucion

def tengo_obj_pegado(jugador_x, jugador_y, pos_caja_x, pos_caja_y):
#me fijo si tengo otro objetivo alineado y lo empujo para adentro

    aux_x = jugador_x - pos_caja_x
    delta_x = pos_caja_x - aux_x
    aux_y = jugador_y - pos_caja_y
    delta_y = pos_caja_y - aux_y
    if(data[delta_x][delta_y]=='.'):
        data[pos_caja_x][pos_caja_y] = '.'
        data[jugador_x][jugador_y] = ' '
        pos_caja_x = delta_x
        pos_caja_y = delta_y
        jugador_x = jugador_x + aux_x
        jugador_y = jugador_y + aux_y

    return pos_caja_x, pos_caja_y, jugador_x, jugador_y

def quito_objetivo(pos_caja_x, pos_caja_y):
    pos = 0 
    for i in objetivos_ubicacion:
        if (i[0]==pos_caja_x and i[1]==pos_caja_y):
            objetivos_ubicacion.pop(pos)
        pos = pos + 1

def imprimo_pasos(solucion, caja, fil_max, col_max, jugador_x, jugador_y):

    pos_caja_x = caja[0]
    pos_caja_y = caja[1]
    #Me fijo adonde tiene que ir el jugador para empezar a empujar la caja
    nodo = solucion.pop()   
    delta_x = pos_caja_x - nodo[0]
    delta_y = pos_caja_y - nodo[1]
    solucion.append(nodo)
    voy_x = pos_caja_x + delta_x
    voy_y = pos_caja_y + delta_y

    #imprimir_estado(data)

    if (jugador_x != voy_x and jugador_y != voy_y):
        #Si el jugador no esta en la posicion deseada:
        costo, jugador_x, jugador_y = voy_para_alla(jugador_x, jugador_y, voy_x, voy_y, fil_max, col_max)
    else:
        imprimir_estado(data)

    while(solucion):
        nodo = solucion.pop()
        if(estan_alineados(jugador_x, jugador_y, 
                            pos_caja_x, pos_caja_y, 
                            nodo[0], nodo[1])):

            data[jugador_x][jugador_y]= ' '
            jugador_x = pos_caja_x
            jugador_y = pos_caja_y        
            pos_caja_x = nodo[0]
            pos_caja_y = nodo[1]
            data[jugador_x][jugador_y]= '@'
            data[pos_caja_x][pos_caja_y] = '$'
            imprimir_estado(data)
        else:
            #print('no alineados')
            aux_x = jugador_x
            aux_y = jugador_y
            delta_x = pos_caja_x - nodo[0]
            delta_y = pos_caja_y - nodo[1]
            #el jugador bordea la caja en 2 movimientos
            if data[jugador_x + delta_x][jugador_y + delta_y]!= '#':
                #print('primer paso')
                data[jugador_x][jugador_y]= ' '
                jugador_x = jugador_x + delta_x
                jugador_y = jugador_y + delta_y
                data[jugador_x][jugador_y]= '@'
                imprimir_estado(data)
                #print('segundo paso')
                delta_x = aux_x - pos_caja_x
                delta_y = aux_y - pos_caja_y 
                data[jugador_x][jugador_y]= ' '
                jugador_x = jugador_x - delta_x
                jugador_y = jugador_y - delta_y
                data[jugador_x][jugador_y]= '@'
                imprimir_estado(data)
            #hay paredes, empiezo a buscar como llegar a la caja
            else:
                delta_x = pos_caja_x - nodo[0]
                delta_y = pos_caja_y - nodo[1]
                voy_x = pos_caja_x + delta_x
                voy_y = pos_caja_y + delta_y
                # print('camino largo')
                # print(delta_x, delta_y, pos_caja_x, pos_caja_y, nodo, voy_x, voy_y)
                nuevo_costo, jugador_x, jugador_y = voy_para_alla(jugador_x, jugador_y, voy_x, voy_y, fil_max, col_max)                
            
            #cuando ya están alineados
            data[jugador_x][jugador_y]= ' '
            data[pos_caja_x][pos_caja_y] = '@'
            data[nodo[0]][nodo[1]]= '$'

            jugador_x = pos_caja_x
            jugador_y = pos_caja_y
            pos_caja_x = nodo[0]
            pos_caja_y = nodo[1]
            imprimir_estado(data)

    #antes de ubicar la caja en el objetivo, me fijo si tengo otro objetivo pegado
    pos_caja_x, pos_caja_y, jugador_x, jugador_y = tengo_obj_pegado(jugador_x, jugador_y, pos_caja_x, pos_caja_y)
        
    # saco el objetivo de la lista de objetivos
    data[jugador_x][jugador_y]= '@'
    data[pos_caja_x][pos_caja_y] = '*'
    imprimir_estado(data)
    quito_objetivo(pos_caja_x,pos_caja_y)

    return jugador_x, jugador_y


def aplico_heuristica (sucesores, heuristica):
    #calculo costo a los sucesores
    #devuelvo la bolsa de sucesores ordenada de mayor a menor costo
    list_mayor_a_menor = []

    #TO DO
    #que objetivo elijo?
    voy_x = objetivos_ubicacion[0][0]
    voy_y = objetivos_ubicacion[0][1]
    for aux_sucesor in sucesores:
        if heuristica == 'Manhattan':
            distance = abs(voy_x - aux_sucesor[0]) + abs(voy_y - aux_sucesor[1])
        if heuristica == 'Euclidea':
            distance = math.sqrt((voy_x - aux_sucesor[0])**2 + (voy_y - aux_sucesor[1])**2)
            
        list_mayor_a_menor.append((distance, aux_sucesor))

    resultado = []
    if (len(list_mayor_a_menor) > 1):
        list_mayor_a_menor = sorted(list_mayor_a_menor, key = lambda x: (x[0], x[1]), reverse = True)   

    for i in list_mayor_a_menor:
        resultado.append(i[1])
    #print('le mando ', resultado)
    return resultado 

def costo_heuristica(heuristica, n):

    voy_x = objetivos_ubicacion[0][0]
    voy_y = objetivos_ubicacion[0][1]

    if heuristica == 'Manhattan':
        distance = abs(voy_x - n[0]) + abs(voy_y - n[1])
    if heuristica == 'Euclidea':
        distance = math.sqrt((voy_x - n[0])**2 + (voy_y - n[1])**2)

    return distance

def quitar_objetivo(n):
    pos = 0
    for i in objetivos_ubicacion:
        if (i[0]==n[0] and i[1]==n[1]):
           objetivos_ubicacion.remove(i)
           pos = pos + 1

def algoritmo_busqueda (metodo, heuristica, nodo, fil_max, col_max, jugador_x, jugador_y):
    empiezo = datetime.now()

    #1. Crear Tr, Fr y Exp inicialmente vacíos.
    
    Tr = [] #El camino
    visited = [] #Nodos visitados
    Fr = [] #Conjunto frontera
    Exp = [] #Nodos explorados
    mi_arbol=[]#Guardo niveles y nodos
    
    #2. Insertar nodo inicial n0 en Tr y Fr.
    Fr.append(nodo)
    Exp.append(nodo)
    visited.append(nodo)
    mi_arbol.append([nodo])
    nivel = -1    
    costo = 0
    exito = 0
    #3. Mientras Fr no esté vacía… (6 en caso de estar vacía)
    while(Fr):
        #a. Extraer primer nodo de Fr => Nodo n
        n = Fr.pop(0)
   
        #print('tomo ', n)
        
        if (metodo == 'ggs'):
            costo = costo + costo_heuristica(heuristica, n)
        
        #actua guardando los que visito
        Tr.append(n)
        #b. Si n es goal
        if (n in objetivos_ubicacion):       
            # i. Devolver la solución, formada por el arco entre la raíz n0 
            # y el nodo n en Tr. Termina Algoritmo.  
            quitar_objetivo(n)
            solucion = []
            solucion = busco_camino(metodo, mi_arbol, Tr, n, fil_max, col_max)
            exito = 1
            break
    
        # c. Expandir el nodo n, generando los sucesores. Ingresar
        # dichos sucesores en Fr y colocarlos en Tr como nodos
        # sucesores de n.
   
        sucesores = genero_hijos(n, fil_max, col_max)
        if sucesores:
            Exp.append(n)
            #me fijo si n ya esta y guardo los sucesores en el nivel que les corresponde

            nivel = nivel + 1
            # print('nivel ', nivel)
            #print('sucesores: ', sucesores)
            #por si llego a un deadlock, tengo como volver
            #deadlock_mat.append([sucesores, (pos_caja_x, pos_caja_y,pos_jugador_x, pos_jugador_y)])
        
            if (metodo == 'ggs'):
                sucesores = aplico_heuristica (sucesores, heuristica)           
            
            for aux_sucesor in sucesores:
                if aux_sucesor not in visited:
                    
                    if (metodo == 'bfs'):
                        Fr.append(aux_sucesor)
                    elif (metodo == 'dfs' or 'ggs'):
                        Fr.insert(0,aux_sucesor)

                    visited.append(aux_sucesor)
                    costo = costo + 1

            aux = nivel_en_arbol(mi_arbol, n)
            # print('que dice aux y n ', aux, n)
            # print('para los sucesores ', sucesores)
            # print('tamanio del arbol ', len(mi_arbol))
            if (aux + 1 == len(mi_arbol)):
                mi_arbol.append([sucesores])
            else:
                mi_arbol[aux+1].extend([sucesores])

        # 4. Reordenar Fr según un criterio dado (depende del método de
        # # búsqueda).
        
        
        #print(Fr)
    
        # 5. Ir al paso 3.
    print('Costo de la solucion ', costo)
    print('Cantidad de nodos frontera ', len(Fr))
    print('Cantidad de nodos expandidos ', len(Exp[1:]))
    termino = datetime.now()
    delta = termino - empiezo
    print('Tiempo de procesamiento en microsegundos', delta.microseconds) 
    if exito ==1:
        nivel_exito = nivel_en_arbol(mi_arbol, n) + 1
        print('Solucion Encontrada ')
        print('Solucion ', solucion)
        print('Profundidad de la solucion ', nivel_exito)
        #jugador_x, jugador_y = imprimo_pasos(solucion, nodo, fil_max, col_max, jugador_x, jugador_y)
    else:
        print('No hay solucion')
    
    return jugador_x, jugador_y
    
######### MAIN ###########

from datetime import datetime
jugador, fil_max, col_max = genero_estado_inicial('soko7.txt')

imprimir_estado(data)

jugador_x = jugador[0]
jugador_y = jugador[1]
metodo = 'ggs'
heuristica = 'Manhattan'
#heuristica = 'Euclidea'
print('Método ', metodo)
if (metodo == 'ggs'):
    print('Heuristica ', heuristica)

for i in cajas_ubicacion:
    print('Caja ', i)
    jugador_x, jugador_y = algoritmo_busqueda (metodo, heuristica, i, fil_max, col_max, jugador_x, jugador_y)

