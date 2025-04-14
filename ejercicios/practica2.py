def cuenta_grado(grafo_lista):
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''

    '''
    vertices, aristas = grafo_lista
    grados = {v: 0 for v in vertices}

    for origen, destino in aristas:
        grados[origen] += 1
        grados[destino] += 1

    return grados
    '''

    vertices, aristas = grafo_lista
    grados = {}

    for v in vertices:
        grados[v] = 0
    for a, b in aristas:
        grados[a] += 1
        grados[b] += 1

    return grados


def vertice_aislado(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    grados = cuenta_grado(grafo_lista)
    aislados = []

    for v in grados:
        if (grados[v] == 0):
            aislados.append(v)
    
    return aislados

def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    pass

def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    pass
