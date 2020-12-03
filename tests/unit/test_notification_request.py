# -*- coding: utf-8 -*-
import datetime
import unittest

from dateutil import tz

from yookassa_payout.domain.common.currency import Currency
from yookassa_payout.domain.common.data_context import DataContext
from yookassa_payout.domain.notification.error_deposition_notification_request import \
    ErrorDepositionNotificationRequest


class TestNotificationRequest(unittest.TestCase):

    def test_request_cast(self):
        req = ErrorDepositionNotificationRequest()
        req.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        req.request_dt = '2020-03-04T15:39:45.456+03:00'
        req.dst_account = 250000
        req.amount = 10.00
        req.currency = Currency.RUB
        req.error = 0

        self.assertEqual({
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'request_dt': datetime.datetime(2020, 3, 4, 15, 39, 45, 456000, tzinfo=tz.gettz('Europe/Moscow')),
            'dst_account': '250000',
            'amount': 10.0,
            'currency': Currency.RUB,
            'error': 0,
        }, dict(req))

        self.assertEqual(req.context(), DataContext.REQUEST)

    def test_request_setters(self):
        req = ErrorDepositionNotificationRequest({
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'request_dt': '2020-03-04T15:39:45.456+03:00',
            'dst_account': 250000,
            'amount': '10',
            'currency': Currency.RUB,
            'error': '0',
        })

        self.assertIsInstance(req.client_order_id, str)
        self.assertEqual(req.client_order_id, '215d8da0-000f-50be-b000-0003308c89be')

        self.assertIsInstance(req.request_dt, datetime.datetime)
        self.assertEqual(req.request_dt, datetime.datetime(2020, 3, 4, 15, 39, 45, 456000,
                                                           tzinfo=tz.gettz('Europe/Moscow')))

        self.assertIsInstance(req.dst_account, str)
        self.assertEqual(req.dst_account, '250000')

        self.assertIsInstance(req.amount, float)
        self.assertEqual(req.amount, 10.0)

        self.assertIsInstance(req.currency, int)
        self.assertEqual(req.currency, Currency.RUB)

        self.assertIsInstance(req.error, int)
        self.assertEqual(req.error, 0)

        with self.assertRaises(ValueError):
            req.request_dt = 'invalid common_name'

        with self.assertRaises(TypeError):
            req.request_dt = object()

    def test_request_validate(self):
        req = ErrorDepositionNotificationRequest()

        with self.assertRaises(ValueError):
            req.validate()

        req.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        with self.assertRaises(ValueError):
            req.validate()

        req.request_dt = '2020-03-04T15:39:45.456+03:00'
        with self.assertRaises(ValueError):
            req.validate()

        req.request_dt = datetime.datetime(2020, 3, 4, 15, 39, 45, 456000, tzinfo=tz.gettz('Europe/Moscow'))
        with self.assertRaises(ValueError):
            req.validate()

        req.dst_account = '250000'
        with self.assertRaises(ValueError):
            req.validate()

        req.amount = '10'
        with self.assertRaises(ValueError):
            req.validate()

        req.currency = Currency.RUB
        with self.assertRaises(ValueError):
            req.validate()

        req = ErrorDepositionNotificationRequest({
            'request_dt': '2020-03-04T15:39:45.456+03:00',
            'dst_account': 250000,
            'amount': '10',
            'currency': Currency.RUB,
        })
        req.error = 31
        with self.assertRaises(ValueError):
            req.validate()
