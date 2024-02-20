#!/usr/bin/python3
"""
checking if an obj is of a certain class
"""


class a_class:
    """sample class"""
    pass
obj = a_class()

"""Check if obj is an instance of MyClass"""
def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
