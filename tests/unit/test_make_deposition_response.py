# -*- coding: utf-8 -*-
import unittest

from yookassa_payout.domain.common.data_context import DataContext
from yookassa_payout.domain.response.make_deposition_response import MakeDepositionResponse


class TestMakeDepositionResponse(unittest.TestCase):

    def test_response_cast(self):
        req = MakeDepositionResponse()
        req.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        req.error = 123456
        req.tech_message = 'tech_message'
        req.identification = 'identification'
        req.balance = 30

        self.assertEqual({
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'error': 123456,
            'tech_message': 'tech_message',
            'identification': 'identification',
            'balance': 30.0,
        }, dict(req))

    def test_response_setters(self):
        res = MakeDepositionResponse({
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'error': 123456,
            'tech_message': 'tech_message',
            'identification': 'identification',
            'balance': 30,
        })

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

    def test_response_validate(self):
        res = MakeDepositionResponse()

        with self.assertRaises(ValueError):
            res.validate()

        res.error = 250000
        with self.assertRaises(ValueError):
            res.validate()

        res.tech_message = 'tech_message'
        with self.assertRaises(ValueError):
            res.validate()

        res.identification = 'identification'
        with self.assertRaises(ValueError):
            res.validate()

    def test_response_context(self):
        res = MakeDepositionResponse()
        self.assertEqual(res.context(), DataContext.RESPONSE)

    def test_response_map_in(self):
        req = MakeDepositionResponse()
        self.assertEqual(req.map_in(), {
            "status": "status",
            "processedDT": "processed_dt",
            "agentId": "agent_id",
            "clientOrderId": "client_order_id",
            "error": "error",
            "techMessage": "tech_message",
            "identification": "identification",
            "incomeReceiptId": "income_receipt_id",
            "incomeReceiptLink": "income_receipt_link",
            "balance": "balance",
        })
