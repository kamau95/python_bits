#!/usr/bin/python3
"""inherits from"""



def inherits_from(obj, a_class):
    """checking for a subclass"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
