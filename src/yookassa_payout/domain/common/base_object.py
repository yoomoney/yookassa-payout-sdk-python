# -*- coding: utf-8 -*-


class BaseObject(object):
    """
    Base class for data objects.
    A class provides cast to dictionary functionality and set up attributes from dictionary.
    """

    def __init__(self, *args, **kwargs):
        for dictionary in args:
            for key in dictionary:
                setattr(self, self.from_map(key, self.map_in()), dictionary[key])
        for key in kwargs:
            setattr(self, self.from_map(key, self.map_in()), kwargs[key])

    def __iter__(self):
        property_names = [prop for prop in dir(self.__class__) if isinstance(getattr(self.__class__, prop), property)]
        properties = dict((value, getattr(self, value)) for value in property_names if getattr(self, value) is not None)
        # print(properties)
        for prop_name, prop_value in properties.items():
            if isinstance(prop_value, BaseObject):
                yield prop_name, dict(prop_value)
            elif isinstance(prop_value, list):
                list_value = []
                for value in prop_value:
                    if isinstance(value, BaseObject):
                        list_value.append(dict(value)),
                    else:
                        list_value.append(value)
                yield prop_name, list_value
            else:
                yield prop_name, prop_value

    @staticmethod
    def from_map(prop, _map):
        return _map[prop] if prop in _map else prop

    def map_in(self):
        return {}
