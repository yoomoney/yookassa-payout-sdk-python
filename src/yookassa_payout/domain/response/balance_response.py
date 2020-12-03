# -*- coding: utf-8 -*-

from yookassa_payout.domain.response.response_object import ResponseObject


class BalanceResponse(ResponseObject):

    __agent_id = None
    __client_order_id = None
    __balance = None

    @property
    def agent_id(self):
        return self.__agent_id

    @agent_id.setter
    def agent_id(self, value):
        self.__agent_id = int(value)

    @property
    def client_order_id(self):
        return self.__client_order_id

    @client_order_id.setter
    def client_order_id(self, value):
        self.__client_order_id = str(value)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = float(value)

    def validate(self):
        if not self.agent_id:
            self.set_validation_error('Balance agent_id not specified')
        if not self.client_order_id:
            self.set_validation_error('Balance client_order_id not specified')

    def set_validation_error(self, message):
        raise ValueError(message)

    def map_in(self):
        _map = super(BalanceResponse, self).map_in()
        _map.update({
            "agentId": "agent_id",
            "clientOrderId": "client_order_id",
            "balance": "balance",
        })
        return _map
