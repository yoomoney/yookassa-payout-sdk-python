# -*- coding: utf-8 -*-
import sys
import unittest

from unittest.mock import patch

from yookassa_payout.domain.common.client import ApiClient
from yookassa_payout.configuration import Configuration
from yookassa_payout.domain.common.http_verb import HttpVerb
from yookassa_payout.domain.common.keychain import KeyChain
from yookassa_payout.domain.request.request_object import RequestObject


class TestClient(unittest.TestCase):
    pass
    # def setUp(self):
    #     keychain = KeyChain('public_cert', 'private_key', 'key_password')
    #     Configuration.configure(agent_id='test_account_id', keychain=keychain)
    #
    # def test_request(self):
    #     client = ApiClient()
    #     with patch('requests.Session.request') as request_mock:
    #         request_mock.return_value = {
    #             'amount': {'currency': 'RUB', 'value': 1.0},
    #             'created_at': '2017-11-30T15:45:31.130Z',
    #             'id': '21b23b5b-000f-5061-a000-0674e49a8c10',
    #             'metadata': {'float_value': '123.32', 'key': 'data'},
    #             'paid': False,
    #             'payment_method': {'type': 'bank_card'},
    #             'recipient': {'account_id': '156833', 'gateway_id': '468284'},
    #             'status': 'canceled'
    #         }
    #
    #         client.request(HttpVerb.POST, '/path', RequestObject(), {'header': 'header'})
