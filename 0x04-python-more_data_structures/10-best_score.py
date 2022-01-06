#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    laNueva = []
    if matrix:
        for iteradorMatrix in matrix:
            fila = []
            for iteradorContenido in iteradorMatrix:
                fila.append(iteradorContenido * iteradorContenido)
            laNueva.append(fila)
        return (laNueva)
