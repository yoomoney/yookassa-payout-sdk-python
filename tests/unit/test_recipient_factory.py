# -*- coding: utf-8 -*-
import unittest
from yookassa_payout.domain.models.recipients.bank_account_recipient import BankAccountRecipient
from yookassa_payout.domain.models.recipients.bank_card_recipient import BankCardRecipient
from yookassa_payout.domain.models.recipients.recipient import Recipient
from yookassa_payout.domain.models.recipients.recipient_factory import RecipientFactory


class TestRecipientFactory(unittest.TestCase):

    def test_factory_validate(self):

        with self.assertRaises(TypeError):
            RecipientFactory.factory('invalid string')

        with self.assertRaises(TypeError):
            RecipientFactory.factory(123456789)

        with self.assertRaises(TypeError):
            RecipientFactory.factory(['invalid string'])

        with self.assertRaises(ValueError):
            RecipientFactory.factory({
                'invalid_key': 'invalid data'
            })

        r = RecipientFactory.factory({
            'customer_account': 'customer_account'
        })
        self.assertIsInstance(r, BankAccountRecipient)

        r = RecipientFactory.factory({
            'skr_destination_card_synonym': 'skr_destination_card_synonym'
        })
        self.assertIsInstance(r, BankCardRecipient)

        r = RecipientFactory.factory({
            'pof_offer_accepted': True
        })
        self.assertIsInstance(r, Recipient)
