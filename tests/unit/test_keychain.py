# -*- coding: utf-8 -*-
import unittest

from yookassa_payout.domain.common.data_context import DataContext
from yookassa_payout.domain.common.keychain import KeyChain
from yookassa_payout.domain.request.synonym_card_request import SynonymCardRequest


class TestKeyChain(unittest.TestCase):

    def test_keychain_setters(self):
        kc = KeyChain('public_cert', 'private_key', 'key_password')

        self.assertEqual(kc.public_cert, 'public_cert')
        self.assertEqual(kc.private_key, 'private_key')
        self.assertEqual(kc.key_password, 'key_password')

        kc.public_cert = 'public_cert'
        kc.private_key = 'private_key'
        kc.key_password = 'key_password'

        self.assertEqual(kc.public_cert, 'public_cert')
        self.assertEqual(kc.private_key, 'private_key')
        self.assertEqual(kc.key_password, 'key_password')
