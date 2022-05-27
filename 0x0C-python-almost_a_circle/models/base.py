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
        """Saves to csv file
        """

        res = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_file:
            write_to = csv.DictWriter(save_file, res[0].keys())
            write_to.writeheader()
            write_to.writerows(res)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file
        """

        res = []
        res_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for k, v in dict(item).items():
                    res_dict[k] = int(v)
                # formatting with create()
                res.append(cls.create(**res_dict))
        return res
