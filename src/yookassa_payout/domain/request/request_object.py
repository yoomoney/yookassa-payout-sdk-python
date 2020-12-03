# -*- coding: utf-8 -*-
import datetime

from dateutil import parser

from yookassa_payout.domain.common.base_object import BaseObject
from yookassa_payout.domain.common.data_context import DataContext


class RequestObject(BaseObject):
    """
    Base class for request objects
    """

    __request_name = None
    __request_dt = None

    def __init__(self, *args, **kwargs):
        super(RequestObject, self).__init__(*args, **kwargs)
        self.request_dt = datetime.datetime.now()
        self.request_name = 'baseRequest'

    @property
    def request_name(self):
        return self.__request_name

    @request_name.setter
    def request_name(self, value):
        self.__request_name = str(value)

    @property
    def request_dt(self):
        return self.__request_dt

    @request_dt.setter
    def request_dt(self, value):
        if isinstance(value, str):
            try:
                self.__request_dt = parser.parse(value)  # , '%Y-%m-%dT%H:%M:%S.%f%z'
            except Exception:
                raise ValueError('Invalid request_dt value')
        elif isinstance(value, datetime.datetime):
            self.__request_dt = value
        else:
            raise TypeError('Invalid request_dt value type')

    @staticmethod
    def context():
        return DataContext.REQUEST

    def map(self):
        """
        Mapping request data to protocol
        """
        return {
            "requestDT": self.request_dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }

    def validate(self):
        if not self.request_name:
            self.set_validation_error('RequestObject request_name not specified')

    def set_validation_error(self, message):
        raise ValueError(message)
