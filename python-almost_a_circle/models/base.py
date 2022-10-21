#!/usr/bin/python3
"""Module that contains "Base" class"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))
