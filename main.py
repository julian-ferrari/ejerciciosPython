from ejercicios.practica1 import lee_grafo_stdin
from ejercicios.practica2 import cuenta_grado, vertice_aislado, componentes_conexas

def main():
    entrada = ['5', 'A', 'B', 'C', 'D', 'E', 'A B', 'B C', 'C B']
    grafo = lee_grafo_stdin(entrada)
    resultado = cuenta_grado(grafo)
    aislado = vertice_aislado(grafo)
    comp_conexas = componentes_conexas(grafo)
    print(grafo)
    print(resultado)
    print(aislado)
    print(comp_conexas)


if __name__ == '__main__':
    main()