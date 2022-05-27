#!/usr/bin/python3
"""this is a Rectangle class"""


from models.base import Base
"""superclass rectangle"""


class Rectangle(Base):
    """subclass Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        """initialize instance attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width return"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get heigth return"""
        return self.__height

    @height.setter
    def height(self, value):
        """set heigth"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x return"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y return"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """find area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print in stdout the Rectangle instance with the character #"""
        print('\n' * self.__y, end='')
        for height in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """return string to be printed"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assingns an argument to each attribute"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """create a dictionary representation of a rectangle"""
        return {"x": self.__x, "y": self.y, "id": self.id,
                "height": self.__height, "width": self.__width}
