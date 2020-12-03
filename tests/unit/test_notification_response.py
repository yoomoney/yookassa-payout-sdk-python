# -*- coding: utf-8 -*-
import datetime
import unittest

from dateutil import tz

from yookassa_payout.domain.common.data_context import DataContext
from yookassa_payout.domain.notification.error_deposition_notification_request import \
    ErrorDepositionNotificationRequest
from yookassa_payout.domain.notification.error_deposition_notification_response import \
    ErrorDepositionNotificationResponse


class TestNotificationResponse(unittest.TestCase):

    def test_response_cast(self):
        res = ErrorDepositionNotificationResponse()
        res.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        res.processed_dt = '2020-03-04T15:39:45.456+03:00'
        res.status = 0

        self.assertEqual({
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'processed_dt': datetime.datetime(2020, 3, 4, 15, 39, 45, 456000, tzinfo=tz.gettz('Europe/Moscow')),
            'status': 0,
        }, dict(res))

        self.assertEqual(res.context(), DataContext.RESPONSE)

    def test_response_setters(self):
        req = ErrorDepositionNotificationResponse({
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'status': '0',
        })

        self.assertIsInstance(req.client_order_id, str)
        self.assertEqual(req.client_order_id, '215d8da0-000f-50be-b000-0003308c89be')

        self.assertIsInstance(req.processed_dt, datetime.datetime)

        self.assertIsInstance(req.status, int)
        self.assertEqual(req.status, 0)

        with self.assertRaises(ValueError):
            req.processed_dt = 'invalid common_name'

        with self.assertRaises(TypeError):
            req.processed_dt = object()

    def test_response_validate(self):
        req = ErrorDepositionNotificationResponse()

        with self.assertRaises(ValueError):
            req.validate()

        req.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        with self.assertRaises(ValueError):
            req.validate()

        req.processed_dt = '2020-03-04T15:39:45.456+03:00'
        with self.assertRaises(ValueError):
            req.validate()

        req.processed_dt = datetime.datetime(2020, 3, 4, 15, 39, 45, 456000, tzinfo=tz.gettz('Europe/Moscow'))
        with self.assertRaises(ValueError):
            req.validate()

        req = ErrorDepositionNotificationRequest({
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
        })
        req.status = 0
        with self.assertRaises(ValueError):
            req.validate()

    def test_response_map(self):
        req = ErrorDepositionNotificationResponse({
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'status': '0',
        })
        self.assertEqual(req.map(), {
            "ErrorDepositionNotificationResponse": {
                "clientOrderId": req.client_order_id,
                "processedDT": req.processed_dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
                "status": req.status,
            }
        })