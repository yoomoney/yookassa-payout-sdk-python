# -*- coding: utf-8 -*-
import datetime
import unittest
from dateutil import tz, parser

from yookassa_payout.domain.models.recipients.recipient import Recipient
from yookassa_payout.domain.request.balance_request import BalanceRequest
from yookassa_payout.domain.request.make_deposition_request import MakeDepositionRequest


class TestBalanceRequest(unittest.TestCase):

    def test_request_cast(self):
        req = BalanceRequest()
        req.agent_id = 123456
        req.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        req.request_dt = '2020-03-04T15:39:45.456+03:00'

        self.assertEqual({
            'agent_id': 123456,
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'request_dt': datetime.datetime(2020, 3, 4, 15, 39, 45, 456000, tzinfo=tz.gettz('Europe/Moscow')),
            'request_name': 'balanceRequest'
        }, dict(req))

    def test_request_setters(self):
        req = BalanceRequest({
            'agent_id': 123456,
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'request_dt': '2020-03-04T15:39:45.456+03:00'
        })

        self.assertIsInstance(req.agent_id, int)
        self.assertIsInstance(req.client_order_id, str)
        self.assertIsInstance(req.request_dt, datetime.datetime)
        self.assertEqual(req.request_name, 'balanceRequest')

        with self.assertRaises(ValueError):
            req.request_dt = 'invalid request_dt'

        with self.assertRaises(TypeError):
            req.request_dt = object()

    def test_request_validate(self):
        req = BalanceRequest()

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

    def test_request_map(self):
        req = BalanceRequest({
            'agent_id': 123456,
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
        })
        self.assertEqual(req.map(), {
            'balanceRequest': {
                "requestDT": req.request_dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
                "agentId": req.agent_id,
                "clientOrderId": req.client_order_id
            }
        })
