# -*- coding: utf-8 -*-


class KeyChain:
    """
    A class for keys store.
    """
    VERSION_DELIMITER = '/'
    PART_DELIMITER = ' '

    __public_cert = None

    __private_key = None

    __key_password = None

    def __init__(self, public_cert, private_key, key_password=''):
        self.public_cert = public_cert
        self.private_key = private_key
        self.key_password = key_password

    @property
    def public_cert(self):
        return self.__public_cert

    @public_cert.setter
    def public_cert(self, value):
        self.__public_cert = str(value)

    @property
    def private_key(self):
        return self.__private_key

    @private_key.setter
    def private_key(self, value):
        self.__private_key = str(value)

    @property
    def key_password(self):
        return self.__key_password

    @key_password.setter
    def key_password(self, value):
        self.__key_password = str(value)
