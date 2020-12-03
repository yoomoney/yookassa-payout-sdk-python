# -*- coding: utf-8 -*-
import unittest

from yookassa_payout.domain.common.data_context import DataContext
from yookassa_payout.domain.response.synonym_card_response import SynonymCardResponse


class TestSynonymCardResponse(unittest.TestCase):

    def test_response_cast(self):
        res = SynonymCardResponse()
        res.panmask = '444444******4448'
        res.synonym = '4878b27eaec2022c5a6a4e82d971a6271bf6fcd8_scn'
        res.reason = 'success'
        res.bank_name = 'Norwegian Visa - Bankgroup'
        res.country_code = '616'
        res.payment_system = 'Visa'
        res.product_name = 'Visa Gold'
        res.product_code = 'P'

        self.assertEqual({
            'panmask': '444444******4448',
            'synonym': '4878b27eaec2022c5a6a4e82d971a6271bf6fcd8_scn',
            'reason': 'success',
            'bank_name': 'Norwegian Visa - Bankgroup',
            'country_code': '616',
            'payment_system': 'Visa',
            'product_name': 'Visa Gold',
            'product_code': 'P',
        }, dict(res))

    def test_response_setters(self):
        res = SynonymCardResponse({
            'panmask': '444444******4448',
            'synonym': '4878b27eaec2022c5a6a4e82d971a6271bf6fcd8_scn',
            'reason': 'success',
            'bank_name': 'Norwegian Visa - Bankgroup',
            'country_code': '616',
            'payment_system': 'Visa',
            'product_name': 'Visa Gold',
            'product_code': 'P',
        })

        self.assertIsInstance(res.panmask, str)
        self.assertEqual(res.panmask, '444444******4448')

        self.assertIsInstance(res.synonym, str)
        self.assertEqual(res.synonym, '4878b27eaec2022c5a6a4e82d971a6271bf6fcd8_scn')

        self.assertIsInstance(res.reason, str)
        self.assertEqual(res.reason, 'success')

        self.assertIsInstance(res.bank_name, str)
        self.assertEqual(res.bank_name, 'Norwegian Visa - Bankgroup')

        self.assertIsInstance(res.country_code, str)
        self.assertEqual(res.country_code, '616')

        self.assertIsInstance(res.payment_system, str)
        self.assertEqual(res.payment_system, 'Visa')

        self.assertIsInstance(res.product_name, str)
        self.assertEqual(res.product_name, 'Visa Gold')

        self.assertIsInstance(res.product_code, str)
        self.assertEqual(res.product_code, 'P')

    def test_response_validate(self):
        res = SynonymCardResponse()

        with self.assertRaises(ValueError):
            res.validate()

        res.bank_name = 'Norwegian Visa - Bankgroup'
        with self.assertRaises(ValueError):
            res.validate()

        res.country_code = '616'
        with self.assertRaises(ValueError):
            res.validate()

        res.payment_system = 'Visa'
        with self.assertRaises(ValueError):
            res.validate()

        res.product_name = 'Visa Gold'
        with self.assertRaises(ValueError):
            res.validate()

        res.product_code = 'P'
        with self.assertRaises(ValueError):
            res.validate()

        res.panmask = '444444******4448'
        with self.assertRaises(ValueError):
            res.validate()

        res.synonym = '4878b27eaec2022c5a6a4e82d971a6271bf6fcd8_scn'
        with self.assertRaises(ValueError):
            res.validate()

        res.synonym = ''
        res.reason = 'success'
        with self.assertRaises(ValueError):
            res.validate()

    def test_response_context(self):
        res = SynonymCardResponse()
        self.assertEqual(res.context(), DataContext.RESPONSE)

    def test_response_map_in(self):
        req = SynonymCardResponse()
        self.assertEqual(req.map_in(), {
            "skr_destinationCardPanmask": "panmask",
            "skr_destinationCardSynonim": "synonym",
            "reason": "reason",
            "skr_destinationCardBankName": "bank_name",
            "skr_destinationCardCountryCode": "country_code",
            "skr_destinationCardPaymentSystem": "payment_system",
            "skr_destinationCardProductName": "product_name",
            "skr_destinationCardProductCode": "product_code",
        })
