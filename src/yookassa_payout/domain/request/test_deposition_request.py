# -*- coding: utf-8 -*-
from yookassa_payout.domain.request.deposition_request import DepositionRequest


class TestDepositionRequest(DepositionRequest):

    def __init__(self, *args, **kwargs):
        super(TestDepositionRequest, self).__init__(*args, **kwargs)
        self.request_name = 'testDeposition'

    def map(self):
        self.validate()
        _map = super(TestDepositionRequest, self).map()
        return {self.request_name + 'Request': _map}
