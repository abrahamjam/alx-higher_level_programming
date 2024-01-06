#!/usr/bin/python3
"""Defines a function that prints a name"""

def say_my_name(first_name, last_name=""):
    """prints a name.
    Args:
        first_name(str): first name
        last_name(str): last name
    Raises:
        TypeError:if either first_name or last_name is not a string.
    """
    if isinstance(first_name, str):
        raise TypeError("first name must be string")
    if isinstance(last_name, str):
        raise TypeError("last names must be string")
    print("My name is {} {}".format(first_name, last_name))
