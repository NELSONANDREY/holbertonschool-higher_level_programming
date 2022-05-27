#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square():
    """Inicializando la funcion inicial.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value=0):
        """controlamos las exepciones"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Posicion del valor"""
        return self.__position

    @position.setter
    def position(self, value):
        """Verificamos los errores posibles del valor.
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returnamos el valor de la operacion"""
        return (self.__size * self.__size)

    def my_print(self):
        """Con la condicional verificamos el tamaño y
        con los ciclos imprimimos el cuadrado de ##
        en la posicion dada.
        """
        posi = self.__position
        if self.__size != 0:
            for zero1 in range(0, self.position[1]):
                print()
            for x in range(0, self.size):
                for zero1 in range(0, posi[0]):
                    print(" ", end='')
                for y in range(0, self.size):
                    print("#", end="")
                print()
        else:
            print()
