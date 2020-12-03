# -*- coding: utf-8 -*-
import datetime

from dateutil import parser

from yookassa_payout.domain.common.base_object import BaseObject
from yookassa_payout.domain.common.data_context import DataContext


class ErrorDepositionNotificationRequest(BaseObject):

    __request_dt = None
    __client_order_id = None
    __dst_account = None
    __amount = None
    __currency = None
    __error = None

    def __init__(self, *args, **kwargs):
        super(ErrorDepositionNotificationRequest, self).__init__(*args, **kwargs)

    @staticmethod
    def context():
        return DataContext.REQUEST

    @property
    def request_dt(self):
        return self.__request_dt

    @request_dt.setter
    def request_dt(self, value):
        if isinstance(value, str):
            try:
                self.__request_dt = parser.parse(value)  # '%Y-%m-%dT%H:%M:%S.%f%z'
            except Exception:
                raise ValueError('Invalid request_dt value')
        elif isinstance(value, datetime.datetime):
            self.__request_dt = value
        else:
            raise TypeError('Invalid request_dt value type')

    @property
    def client_order_id(self):
        return self.__client_order_id

    @client_order_id.setter
    def client_order_id(self, value):
        self.__client_order_id = str(value)

    @property
    def dst_account(self):
        return self.__dst_account

    @dst_account.setter
    def dst_account(self, value):
        self.__dst_account = str(value)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = float(value)

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = int(value)

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, value):
        self.__error = int(value)

    def validate(self):
        if self.request_dt is None:
            self.__set_validation_error('ErrorDepositionNotificationRequest request_dt not specified')
        if self.client_order_id is None:
            self.__set_validation_error('ErrorDepositionNotificationRequest client_order_id not specified')
        if self.dst_account is None:
            self.__set_validation_error('ErrorDepositionNotificationRequest dst_account not specified')
        if self.amount is None:
            self.__set_validation_error('ErrorDepositionNotificationRequest amount not specified')
        if self.currency is None:
            self.__set_validation_error('ErrorDepositionNotificationRequest currency not specified')
        if self.error is None:
            self.__set_validation_error('ErrorDepositionNotificationRequest error not specified')

    def __set_validation_error(self, message):
        raise ValueError(message)

    def map_in(self):
        _map = super(ErrorDepositionNotificationRequest, self).map_in()
        _map.update({
            "requestDT": "request_dt",
            "clientOrderId": "client_order_id",
            "dstAccount": "dst_account",
            "amount": "amount",
            "currency": "currency",
            "error": "error",
        })
        return _map
