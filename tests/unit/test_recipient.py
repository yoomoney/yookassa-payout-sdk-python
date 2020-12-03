# -*- coding: utf-8 -*-
import unittest
from yookassa_payout.domain.models.recipients.recipient import Recipient


class TestRecipient(unittest.TestCase):

    def test_recipient_cast(self):
        rec = Recipient()
        rec.pof_offer_accepted = True

        self.assertEqual({'pof_offer_accepted': True}, dict(rec))

    def test_recipient_setters(self):
        rec = Recipient({'pof_offer_accepted': True})

        self.assertIsInstance(rec.pof_offer_accepted, bool)
        self.assertEqual(rec.pof_offer_accepted, True)

        with self.assertRaises(ValueError):
            rec.pof_offer_accepted = 'invalid pof_offer_accepted'

    def test_recipient_map(self):
        rec = Recipient({
            'pof_offer_accepted': True,
        })
        self.assertEqual(rec.map(), {
            "pof_offerAccepted": [str(int(rec.pof_offer_accepted))],
        })
