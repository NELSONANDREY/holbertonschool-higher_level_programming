#!/usr/bin/python3
"""Este modulo tiene una funcion que
compara un objeto con una instancia"""


def is_kind_of_class(obj, a_class):
    """Returna verdadero si el obj es una
    instancia de a_clase, si no falso"""
    return isinstance(obj, a_class)
