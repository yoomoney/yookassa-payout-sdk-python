# -*- coding: utf-8 -*-
from yookassa_payout.domain.response.response_object import ResponseObject


class DepositionResponse(ResponseObject):

    __client_order_id = None
    __error = None
    __tech_message = None
    __identification = None
    __income_receipt_id = None
    __income_receipt_link = None

    @property
    def client_order_id(self):
        return self.__client_order_id

    @client_order_id.setter
    def client_order_id(self, value):
        self.__client_order_id = str(value)

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, value):
        self.__error = int(value)

    @property
    def tech_message(self):
        return self.__tech_message

    @tech_message.setter
    def tech_message(self, value):
        self.__tech_message = str(value)

    @property
    def identification(self):
        return self.__identification

    @identification.setter
    def identification(self, value):
        self.__identification = str(value)

    @property
    def income_receipt_id(self):
        return self.__income_receipt_id

    @income_receipt_id.setter
    def income_receipt_id(self, value):
        self.__income_receipt_id = str(value)

    @property
    def income_receipt_link(self):
        return self.__income_receipt_link

    @income_receipt_link.setter
    def income_receipt_link(self, value):
        self.__income_receipt_link = str(value)

    def validate(self):
        if not self.client_order_id:
            self.set_validation_error('DepositionResponse client_order_id not specified')

    def set_validation_error(self, message):
        raise ValueError(message)

    def map_in(self):
        _map = super(DepositionResponse, self).map_in()
        _map.update({
            "agentId": "agent_id",
            "clientOrderId": "client_order_id",
            "error": "error",
            "techMessage": "tech_message",
            "identification": "identification",
            "incomeReceiptId": "income_receipt_id",
            "incomeReceiptLink": "income_receipt_link",
        })
        return _map
