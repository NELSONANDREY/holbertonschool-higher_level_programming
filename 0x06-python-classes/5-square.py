#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square():
    """Inicializando la funcion inicial.
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        """controlamos las exepciones
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returnamos el valor de la operacion"""
        return (self.__size * self.__size)

    def my_print(self):
        """Con la condicional verificamos el tamaño y
        con los ciclos imprimimos el cuadrado de ##
        """
        if self.__size == 0:
            print()
        else:
            for x in range(0, self.__size):
                for y in range(0, self.__size):
                    print("#", end="")
                print()
