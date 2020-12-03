# -*- coding: utf-8 -*-
from yookassa_payout.domain.models.recipients.recipient import Recipient
from yookassa_payout.domain.models.recipients.recipient_factory import RecipientFactory
from yookassa_payout.domain.request.deposition_request import DepositionRequest


class MakeDepositionRequest(DepositionRequest):

    __payment_params = None

    def __init__(self, *args, **kwargs):
        super(MakeDepositionRequest, self).__init__(*args, **kwargs)
        self.request_name = 'makeDeposition'

    @property
    def payment_params(self):
        return self.__payment_params

    @payment_params.setter
    def payment_params(self, value):
        if isinstance(value, Recipient):
            self.__payment_params = value
        elif isinstance(value, dict):
            self.__payment_params = RecipientFactory.factory(value)
        else:
            raise TypeError('Invalid payment_params value type')

    def validate(self):
        super(MakeDepositionRequest, self).validate()
        if not self.payment_params:
            self.set_validation_error('Deposition payment_params not specified')

    def map(self):
        _map = super(MakeDepositionRequest, self).map()
        if self.payment_params:
            _map.update({
                "paymentParams": self.payment_params.map()
            })
        return {self.request_name + 'Request': _map}
