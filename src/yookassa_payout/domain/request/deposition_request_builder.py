# -*- coding: utf-8 -*-
from yookassa_payout.domain.exceptions.api_error import ApiError
from yookassa_payout.domain.request.make_deposition_request import MakeDepositionRequest
from yookassa_payout.domain.request.test_deposition_request import TestDepositionRequest


class DepositionRequestBuilder:

    REQUEST_TEST = 'testDeposition'
    REQUEST_MAKE = 'makeDeposition'

    @classmethod
    def build(cls, params):
        if cls.REQUEST_TEST in params:
            return TestDepositionRequest(params[cls.REQUEST_TEST])
        elif cls.REQUEST_MAKE in params:
            return MakeDepositionRequest(params[cls.REQUEST_MAKE])
        else:
            raise ApiError('Unsupported data format!')
