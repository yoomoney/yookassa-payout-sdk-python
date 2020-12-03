# -*- coding: utf-8 -*-
import unittest

from yookassa_payout.domain.common.context import Context
from yookassa_payout.domain.common.error_converter import ErrorConverter
from yookassa_payout.domain.exceptions.api_error import ApiError


class TestErrorConverter(unittest.TestCase):

    def test_get_list(self):
        self.assertIsInstance(ErrorConverter.get_error_list(), dict)

    def test_get_message(self):
        self.assertEqual('Account closed.', ErrorConverter.get_error_message(40))
        self.assertEqual('The operation amount is too small.', ErrorConverter.get_error_message(46))

        with self.assertRaises(ApiError):
            ErrorConverter.get_error_message(1)
