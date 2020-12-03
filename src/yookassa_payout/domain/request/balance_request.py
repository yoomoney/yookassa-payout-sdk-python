# -*- coding: utf-8 -*-
from yookassa_payout.domain.request.request_object import RequestObject


class BalanceRequest(RequestObject):

    __agent_id = None
    __client_order_id = None

    def __init__(self, *args, **kwargs):
        super(BalanceRequest, self).__init__(*args, **kwargs)
        self.request_name = 'balanceRequest'

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

    def validate(self):
        super(BalanceRequest, self).validate()
        if not self.agent_id:
            self.set_validation_error('Balance agent_id not specified')
        if not self.client_order_id:
            self.set_validation_error('Balance client_order_id not specified')

    def map(self):
        _map = super(BalanceRequest, self).map()
        _map.update({
            "agentId": self.agent_id,
            "clientOrderId": self.client_order_id
        })
        return {self.request_name: _map}
