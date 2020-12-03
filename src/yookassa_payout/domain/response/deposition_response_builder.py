# -*- coding: utf-8 -*-
from yookassa_payout.domain.exceptions.api_error import ApiError
from yookassa_payout.domain.response.make_deposition_response import MakeDepositionResponse
from yookassa_payout.domain.response.test_deposition_response import TestDepositionResponse


class DepositionResponseBuilder:

    RESPONSE_TEST = 'testDeposition'
    RESPONSE_MAKE = 'makeDeposition'

    @classmethod
    def build(cls, data):
        if cls.RESPONSE_TEST + 'Response' in data:
            return TestDepositionResponse(data[cls.RESPONSE_TEST + 'Response'])
        elif cls.RESPONSE_MAKE + 'Response' in data:
            return MakeDepositionResponse(data[cls.RESPONSE_MAKE + 'Response'])
        else:
            raise ApiError('Unknown response')
