# -*- coding: utf-8 -*-
import datetime

from dateutil import parser

from yookassa_payout.domain.common.base_object import BaseObject
from yookassa_payout.domain.common.data_context import DataContext


class ResponseObject(BaseObject):
    """
    Base class for request objects
    """
    __processed_dt = None

    __status = None

    @property
    def processed_dt(self):
        return self.__processed_dt

    @processed_dt.setter
    def processed_dt(self, value):
        if isinstance(value, str):
            self.__processed_dt = parser.parse(value)
        elif isinstance(value, datetime.datetime):
            self.__processed_dt = value
        else:
            raise TypeError('Invalid request_dt value type')

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = int(value)

    @staticmethod
    def context():
        return DataContext.RESPONSE

    def map_in(self):
        return {
            "status": "status",
            "processedDT": "processed_dt"
        }
