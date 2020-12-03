# -*- coding: utf-8 -*-
import unittest

from yookassa_payout.domain.common.data_context import DataContext
from yookassa_payout.domain.response.balance_response import BalanceResponse


class TestBalanceResponse(unittest.TestCase):

    def test_response_cast(self):
        req = BalanceResponse()
        req.agent_id = 123456
        req.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        req.balance = '10'

        self.assertEqual({
            'agent_id': 123456,
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'balance': 10.0,
        }, dict(req))

    def test_response_setters(self):
        res = BalanceResponse({
            'agentId': '123456',
            'clientOrderId': '215d8da0-000f-50be-b000-0003308c89be',
            'balance': 10,
        })

        self.assertIsInstance(res.agent_id, int)
        self.assertEqual(res.agent_id, 123456)

        self.assertIsInstance(res.client_order_id, str)
        self.assertEqual(res.client_order_id, '215d8da0-000f-50be-b000-0003308c89be')

        self.assertIsInstance(res.balance, float)
        self.assertEqual(res.balance, 10.0)

    def test_response_validate(self):
        req = BalanceResponse()

        with self.assertRaises(ValueError):
            req.validate()

        req.agent_id = 250000
        with self.assertRaises(ValueError):
            req.validate()

        req.agent_id = 0
        req.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        with self.assertRaises(ValueError):
            req.validate()

        req.agent_id = 250000
        req.client_order_id = ''
        with self.assertRaises(ValueError):
            req.validate()

    def test_response_context(self):
        res = BalanceResponse()
        self.assertEqual(res.context(), DataContext.RESPONSE)

    def test_response_map_in(self):
        req = BalanceResponse()
        self.assertEqual(req.map_in(), {
            "processedDT": "processed_dt",
            "status": "status",
            "agentId": "agent_id",
            "clientOrderId": "client_order_id",
            "balance": "balance",
        })
