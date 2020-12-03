# -*- coding: utf-8 -*-
"""

"""

import re

from yookassa_payout.domain.common.base_object import BaseObject


class Organization(BaseObject):

    __country_name = 'RU'
    __state = 'Russia'
    __locality = None
    __org_name = None
    __org_unit_name = None
    __common_name = None
    __email = None

    @property
    def country_name(self):
        return self.__country_name

    @country_name.setter
    def country_name(self, value):
        self.__country_name = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def locality(self):
        return self.__locality

    @locality.setter
    def locality(self, value):
        value = '-' if not value else value
        self.__locality = value

    @property
    def org_name(self):
        return self.__org_name

    @org_name.setter
    def org_name(self, value):
        self.__org_name = value

    @property
    def org_unit_name(self):
        return self.__org_unit_name

    @org_unit_name.setter
    def org_unit_name(self, value):
        value = '-' if not value else value
        self.__org_unit_name = value

    @property
    def common_name(self):
        return self.__common_name

    @common_name.setter
    def common_name(self, value):
        cast_value = str(value).replace('/business/', '')
        if re.match(r"^[a-z]+$", cast_value):
            self.__common_name = '/business/' + cast_value
        else:
            raise ValueError('Invalid common_name value')

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        cast_value = str(value)
        if re.match(r"^[^@]+@[^@]+\.[^@]+$", cast_value):
            self.__email = cast_value
        else:
            raise ValueError('Invalid email value type')

    def validate(self):
        if not self.country_name:
            self.__set_validation_error('Organization country_name not specified')
        if not self.state:
            self.__set_validation_error('Organization state not specified')
        if not self.org_name:
            self.__set_validation_error('Organization org_name not specified')
        if not self.common_name:
            self.__set_validation_error('Organization common_name not specified')
        if not self.email:
            self.__set_validation_error('Organization email not specified')

    def verify(self):
        if not self.common_name or not self.email or not self.org_name or not self.country_name or not self.state:
            return False
        else:
            return True

    def __set_validation_error(self, message):
        raise ValueError(message)
