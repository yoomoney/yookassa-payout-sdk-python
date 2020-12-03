# -*- coding: utf-8 -*-
import unittest

from yookassa_payout.domain.exceptions.api_error import ApiError
from yookassa_payout.domain.response.deposition_response_builder import DepositionResponseBuilder
from yookassa_payout.domain.response.make_deposition_response import MakeDepositionResponse
from yookassa_payout.domain.response.test_deposition_response import TestDepositionResponse \
    as TDepositionResponse


class TestDepositionResponseBuilder(unittest.TestCase):

    def test_build(self):
        res = DepositionResponseBuilder.build({
            'testDepositionResponse': {
                'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
                'error': 123456,
                'tech_message': 'tech_message',
                'identification': 'identification',
            }
        })

        self.assertIsInstance(res, TDepositionResponse)

        self.assertIsInstance(res.client_order_id, str)
        self.assertEqual(res.client_order_id, '215d8da0-000f-50be-b000-0003308c89be')

        self.assertIsInstance(res.error, int)
        self.assertEqual(res.error, 123456)

        self.assertIsInstance(res.tech_message, str)
        self.assertEqual(res.tech_message, 'tech_message')

        self.assertIsInstance(res.identification, str)
        self.assertEqual(res.identification, 'identification')

        res = DepositionResponseBuilder.build({
            'makeDepositionResponse': {
                'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
                'error': 123456,
                'tech_message': 'tech_message',
                'identification': 'identification',
                'balance': 30,
            }
        })

        self.assertIsInstance(res, MakeDepositionResponse)

        self.assertIsInstance(res.client_order_id, str)
        self.assertEqual(res.client_order_id, '215d8da0-000f-50be-b000-0003308c89be')

        self.assertIsInstance(res.error, int)
        self.assertEqual(res.error, 123456)

        self.assertIsInstance(res.tech_message, str)
        self.assertEqual(res.tech_message, 'tech_message')

        self.assertIsInstance(res.identification, str)
        self.assertEqual(res.identification, 'identification')

        self.assertIsInstance(res.balance, float)
        self.assertEqual(res.balance, 30.0)

        with self.assertRaises(ApiError):
            res = DepositionResponseBuilder.build({
                'fakeDeposition': {}
            })
