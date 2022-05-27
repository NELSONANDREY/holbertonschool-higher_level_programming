#!/usr/bin/python3
""""this is a Square class"""


from models.rectangle import Rectangle
"""superclass Rectangle"""


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize instance attributes"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """get size return"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """return string to be printed"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """assingns an argument to each attribute"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """create a dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.width,
                "y": self.y}
