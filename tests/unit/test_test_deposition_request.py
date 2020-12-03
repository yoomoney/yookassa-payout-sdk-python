# -*- coding: utf-8 -*-
import datetime
import unittest

from dateutil import tz, parser

from yookassa_payout.domain.common.currency import Currency
from yookassa_payout.domain.request.test_deposition_request import TestDepositionRequest as TDepositionRequest


class TestTestDepositionRequest(unittest.TestCase):

    def test_request_cast(self):
        request = TDepositionRequest()
        request.agent_id = 250000
        request.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        request.request_dt = '2020-03-04T15:39:45.456+03:00'

        self.assertEqual({
            'agent_id': 250000,
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'request_dt': datetime.datetime(2020, 3, 4, 15, 39, 45, 456000, tzinfo=tz.gettz('Europe/Moscow')),
            'request_name': 'testDeposition'
        }, dict(request))

    def test_request_setters(self):
        request = TDepositionRequest({
            'agent_id': 250000,
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'request_dt': '2020-03-04T15:39:45.456+03:00'
        })

        self.assertIsInstance(request.agent_id, int)
        self.assertIsInstance(request.request_dt, datetime.datetime)
        self.assertEqual(request.request_name, 'testDeposition')

        with self.assertRaises(ValueError):
            request.request_dt = 'invalid request_dt'

        with self.assertRaises(TypeError):
            request.request_dt = object()

    def test_request_validate(self):
        request = TDepositionRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.agent_id = 250000
        with self.assertRaises(ValueError):
            request.validate()

        request.agent_id = 0
        request.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        with self.assertRaises(ValueError):
            request.validate()

        request.agent_id = 250000
        request.client_order_id = ''
        with self.assertRaises(ValueError):
            request.validate()

    def test_request_map(self):
        request = TDepositionRequest(self.create_test_params())
        self.assertEqual(request.map(), {
            'testDepositionRequest': {
                "requestDT": request.request_dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
                "agentId": 250000,
                "clientOrderId": '215d8da0-000f-50be-b000-0003308c89be',
                "dstAccount": "41001614575714",
                "amount": format(10.0, ".2f"),
                "currency": Currency.RUB,
                "contract": "Зачисление на кошелек",
            }
        })

    @staticmethod
    def create_test_params():
        return {
            "agent_id": 250000,
            "client_order_id": '215d8da0-000f-50be-b000-0003308c89be',
            "dst_account": "41001614575714",
            "amount": 10.00,
            "currency": Currency.RUB,
            "contract": "Зачисление на кошелек",
        }
