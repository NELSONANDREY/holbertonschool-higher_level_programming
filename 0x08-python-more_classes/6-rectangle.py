#!/usr/bin/python3
"""
Definimos la clase rectangulo
"""


class Rectangle():
    """Definimos el rectangulo"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inicializamos una instacia de rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Obtiene el ancho de una instacia de rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Verfiicamos el ancho de una instancia"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtenemos la altura de una instacia de rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Verificams la altura de una instacia"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula el area de una instancea"""
        return self.__width * self.__height

    def perimeter(self):
        """Calcula el perimetro de una instancea"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Imprime el rectangulo con el caracter #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            str(self.print_symbol) * self.__width for i in range(self.__height)
        )

    def __repr__(self):
        """Para poder recrear una nueva instancia,
        devolvemos la representacion de la cadena"""
        return ("Rectangle ({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Con el metodo del destruimos
        la instancia en cuestion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Encuentra el rectangulo mas grande basado en el area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
