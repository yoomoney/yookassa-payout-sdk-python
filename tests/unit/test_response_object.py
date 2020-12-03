# -*- coding: utf-8 -*-
import datetime
import unittest

from dateutil import tz

from yookassa_payout.domain.common.data_context import DataContext
from yookassa_payout.domain.response.response_object import ResponseObject


class TestResponseObject(unittest.TestCase):

    def test_response_cast(self):
        res = ResponseObject({
            'status': 0,
            'processed_dt': '2020-03-04T15:39:45.456+03:00',
        })

        self.assertEqual({
            'status': 0,
            'processed_dt': datetime.datetime(2020, 3, 4, 15, 39, 45, 456000, tzinfo=tz.gettz('Europe/Moscow')),
        }, dict(res))

    def test_response_setters(self):
        res = ResponseObject()
        res.status = 0
        res.processed_dt = '2020-03-04T15:39:45.456+03:00'

        self.assertIsInstance(res.status, int)
        self.assertEqual(res.status, 0)

        self.assertIsInstance(res.processed_dt, datetime.datetime)
        self.assertEqual(res.processed_dt, datetime.datetime(2020, 3, 4, 15, 39, 45, 456000,
                                                             tzinfo=tz.gettz('Europe/Moscow')))
        res.processed_dt = datetime.datetime(2020, 3, 4, 15, 39, 45, 456000, tzinfo=tz.gettz('Europe/Moscow'))
        self.assertEqual(res.processed_dt, datetime.datetime(2020, 3, 4, 15, 39, 45, 456000,
                                                             tzinfo=tz.gettz('Europe/Moscow')))

        with self.assertRaises(ValueError):
            res.processed_dt = 'invalid processed_dt'

        with self.assertRaises(TypeError):
            res.processed_dt = object()

    def test_response_context(self):
        res = ResponseObject()
        self.assertEqual(res.context(), DataContext.RESPONSE)

    def test_response_map_in(self):
        req = ResponseObject()
        self.assertEqual(req.map_in(), {
            "processedDT": "processed_dt",
            "status": "status"
        })
