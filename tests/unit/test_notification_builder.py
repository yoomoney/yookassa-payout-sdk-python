# -*- coding: utf-8 -*-
import unittest

from yookassa_payout.configuration import Configuration
from yookassa_payout.domain.common.keychain import KeyChain
from yookassa_payout.domain.notification.error_deposition_notification import ErrorDepositionNotification


class TestNotificationBuilder(unittest.TestCase):

    builder = None

    def setUp(self):
        keychain = KeyChain('public_cert', 'private_key', 'key_password')
        Configuration.configure(agent_id='test_account_id', keychain=keychain)
        self.builder = ErrorDepositionNotification()

    def test_notification_input(self):
        pass

    def test_notification_output(self):
        pass
