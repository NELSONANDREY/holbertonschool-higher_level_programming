#!/usr/bin/phyton3
"""This class will be the “base” of all
other classes in this project. """
import json
from curses.textpad import rectangle


class Base:
    """Base of the other shapes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ adding the static method"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns JSON strings in list
        """

        if type(json_string) != str or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes to file with JSON string
        """

        with open(cls.__name__ + ".json", mode="w") as write_file:
            if list_objs is None:
                write_file.write("[]")
            else:
                write_file.write(cls.to_json_string(
                        [element.to_dictionary() for element in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """pendiente comentario"""
        if cls.__name__ == "Rectangle":
            clastmp = cls(1, 1)
        if cls.__name__ == "Square":
            clastmp == cls(1)
        clastmp.update(**dictionary)
        return clastmp

    """ def load_from_file(cls):
        pendiente comentario
                with open(cls.__name__ + ".json", mode="r") as read_file:
    """
