# -*- coding: utf-8 -*-
import unittest

from yookassa_payout.domain.common.data_context import DataContext
from yookassa_payout.domain.request.synonym_card_request import SynonymCardRequest


class TestSynonymCardRequest(unittest.TestCase):

    def test_request_cast(self):
        req = SynonymCardRequest()
        req.destination_card_number = '5555555555554444'
        req.response_format = 'json'
        req.error_url = 'error_url'
        req.success_url = 'success_url'

        self.assertEqual({
            "destination_card_number": "5555555555554444",
            "response_format": "json",
            "error_url": 'error_url',
            "success_url": 'success_url',
        }, dict(req))

        self.assertEqual(req.context(), DataContext.REQUEST)

    def test_request_setters(self):
        request = SynonymCardRequest({
            "destination_card_number": "5555555555554444",
            "response_format": "json",
            "error_url": 'error_url',
            "success_url": 'success_url',
        })

        self.assertEqual(request.destination_card_number, '5555555555554444')
        self.assertEqual(request.response_format, 'json')
        self.assertEqual(request.error_url, 'error_url')
        self.assertEqual(request.success_url, 'success_url')

    def test_request_validate(self):
        req = SynonymCardRequest()

        with self.assertRaises(ValueError):
            req.validate()

        req.response_format = ''
        req.destination_card_number = '5555555555554444'
        with self.assertRaises(ValueError):
            req.validate()

        req.destination_card_number = ''
        req.response_format = 'json'
        with self.assertRaises(ValueError):
            req.validate()

        self.assertEqual(req.verify(), False)

        req.destination_card_number = '5555555555554444'
        self.assertEqual(req.verify(), True)

    def test_request_map(self):
        req = SynonymCardRequest()
        self.assertEqual(req.map(), {
            "skr_destinationCardNumber": req.destination_card_number,
            "skr_responseFormat": req.response_format,
            "skr_errorUrl": req.error_url,
            "skr_successUrl": req.success_url,
        })
