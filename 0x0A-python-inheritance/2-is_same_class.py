#!/usr/bin/python3
"""
Function:
    is_same_class: returns true or false if obj is atype of a class
"""


def is_same_class(obj, a_class):
    """ Function that returns True/False if obj is a type of a_class
    Args:
        obj: object
        a_class: class type
    Returns:
        True if obj is exactly an instance of a class
        False, otherwise
    """

    return (type(obj) is a_class)
