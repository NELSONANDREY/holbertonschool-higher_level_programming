#!/usr/bin/python3
"""this is base class"""


import csv
import json


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):

        """initialize instance attributes"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs  to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(cls.to_json_string(
                        [element.to_dictionary() for element in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """return the list of the json string representing json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(9, 8)
        if cls.__name__ == "Square":
            dummy = cls(9)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """read file in json format and return a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as myfile:
                to_read = myfile.read()
                lists_dic = cls.from_json_string(to_read)
                lists = []
                for k in lists_dic:
                    lists.append(cls.create(**k))
                return lists
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Creamos un archivo .csv y le agregamos
        su contenido"""
        linea = []
        with open(cls._name_ + ".csv", "w") as myfile:
            if list_objs is None or len(list_objs) <= 0:
                myfile.write('[]')
            else:
                if cls._name_ == 'Rectangle':
                    linea = ["id", "width", "height", "x", "y"]
                if cls._name_ == 'Square':
                    linea = ["id", "size", "x", "y"]
            var = csv.DictWriter(myfile, fieldnames=linea)
            for iterador2 in list_objs:
                var.writerow(iterador2.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Lee la funcion save"""
        try:
            with open(cls._name_ + ".csv", "r") as myfile:
                if cls._name_ == 'Rectangle':
                    linea = ["id", "width", "height", "x", "y"]
                if cls._name_ == 'Square':
                    linea = ["id", "size", "x", "y"]
                readeer = csv.DictReader(myfile, fieldnames=linea)
                dcts = [dict([clave, int(valor)]
                        for clave, valor in ltera.items())
                        for ltera in readeer]
                return [cls.create(**dicci) for dicci in dcts]
        except Exception:
            return []
