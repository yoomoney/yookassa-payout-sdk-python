# -*- coding: utf-8 -*-
from yookassa_payout.domain.response.deposition_response import DepositionResponse


class MakeDepositionResponse(DepositionResponse):

    __balance = None

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = float(value)

    def map_in(self):
        _map = super(MakeDepositionResponse, self).map_in()
        _map.update({
            "balance": "balance",
        })
        return _map
