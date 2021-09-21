# -*- coding: utf-8 -*-
import unittest
import datetime

from yookassa_payout.domain.common.currency import Currency
from yookassa_payout.domain.models.recipients.bank_card_recipient import BankCardRecipient


class TestBankCardRecipient(unittest.TestCase):

    def test_recipient_cast(self):
        rec = BankCardRecipient()
        rec.pof_offer_accepted = True
        rec.skr_destination_card_synonym = 'oALesdd_h_YT6pzpJ10Kn5aB.SC.000.201906'
        rec.cps_ym_account = '79653457676'
        rec.pdr_first_name = 'Владимир'
        rec.pdr_middle_name = 'Владимирович'
        rec.pdr_last_name = 'Владимиров'
        rec.pdr_doc_number = '4002109067'
        rec.pdr_doc_issue_date = '1999-07-30'
        rec.pdr_address = 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4'
        rec.pdr_city = 'Санкт-Петербург'
        rec.pdr_country = Currency.RUB
        rec.pdr_postcode = 701152
        rec.pdr_birth_date = '1987-05-24'
        rec.sms_phone_number = '79653457676'

        self.assertEqual({
            'pof_offer_accepted': True,
            'skr_destination_card_synonym': 'oALesdd_h_YT6pzpJ10Kn5aB.SC.000.201906',
            'cps_ym_account': '79653457676',
            'pdr_first_name': 'Владимир',
            'pdr_middle_name': 'Владимирович',
            'pdr_last_name': 'Владимиров',
            'pdr_doc_number': '4002109067',
            'pdr_doc_issue_date': datetime.date(1999, 7, 30),
            'pdr_address': 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4',
            'pdr_city': 'Санкт-Петербург',
            'pdr_country': Currency.RUB,
            'pdr_postcode': 701152,
            'pdr_birth_date': datetime.date(1987, 5, 24),
            'sms_phone_number': '79653457676',
        }, dict(rec))

    def test_recipient_setters(self):
        rec = BankCardRecipient({
            'pof_offer_accepted': True,
            'skr_destination_card_synonym': 'oALesdd_h_YT6pzpJ10Kn5aB.SC.000.201906',
            'cps_ym_account': '79653457676',
            'pdr_first_name': 'Владимир',
            'pdr_middle_name': 'Владимирович',
            'pdr_last_name': 'Владимиров',
            'pdr_doc_number': '4002109067',
            'pdr_doc_issue_date': '1999-07-30',
            'pdr_address': 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4',
            'pdr_city': 'Санкт-Петербург',
            'pdr_country': Currency.RUB,
            'pdr_postcode': 701152,
            'pdr_birth_date': '1987-5-24',
            'sms_phone_number': '+79653457676',
        })

        self.assertIsInstance(rec.pof_offer_accepted, bool)
        self.assertEqual(rec.pof_offer_accepted, True)

        self.assertIsInstance(rec.skr_destination_card_synonym, str)
        self.assertEqual(rec.skr_destination_card_synonym, 'oALesdd_h_YT6pzpJ10Kn5aB.SC.000.201906')

        self.assertIsInstance(rec.cps_ym_account, str)
        self.assertEqual(rec.cps_ym_account, '79653457676')

        self.assertIsInstance(rec.pdr_first_name, str)
        self.assertEqual(rec.pdr_first_name, 'Владимир')

        self.assertIsInstance(rec.pdr_middle_name, str)
        self.assertEqual(rec.pdr_middle_name, 'Владимирович')

        self.assertIsInstance(rec.pdr_last_name, str)
        self.assertEqual(rec.pdr_last_name, 'Владимиров')

        self.assertIsInstance(rec.pdr_doc_number, str)
        self.assertEqual(rec.pdr_doc_number, '4002109067')

        self.assertIsInstance(rec.pdr_doc_issue_date, datetime.date)
        self.assertEqual(rec.pdr_doc_issue_date, datetime.date(1999, 7, 30))

        self.assertIsInstance(rec.pdr_address, str)
        self.assertEqual(rec.pdr_address, 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4')

        self.assertIsInstance(rec.pdr_city, str)
        self.assertEqual(rec.pdr_city, 'Санкт-Петербург')

        self.assertIsInstance(rec.pdr_country, int)
        self.assertEqual(rec.pdr_country, Currency.RUB)

        self.assertIsInstance(rec.pdr_postcode, int)
        self.assertEqual(rec.pdr_postcode, 701152)

        self.assertIsInstance(rec.pdr_birth_date, datetime.date)
        self.assertEqual(rec.pdr_birth_date, datetime.date(1987, 5, 24))

        self.assertIsInstance(rec.sms_phone_number, str)
        self.assertEqual(rec.sms_phone_number, '79653457676')

        with self.assertRaises(ValueError):
            rec.pof_offer_accepted = 'invalid pof_offer_accepted'

        with self.assertRaises(ValueError):
            rec.pdr_doc_issue_date = 'invalid pdr_doc_issue_date'

        with self.assertRaises(TypeError):
            rec.pdr_doc_issue_date = object()

        with self.assertRaises(ValueError):
            rec.pdr_birth_date = 'invalid pdr_birth_date'

        with self.assertRaises(TypeError):
            rec.pdr_birth_date = object()

        with self.assertRaises(ValueError):
            rec.sms_phone_number = 'invalid sms_phone_number'

        with self.assertRaises(ValueError):
            rec.pdr_address = 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4, ' \
                              'пос.Большие Васюки, ул.Комиссара Козявкина, д.4, ' \
                              'пос.Большие Васюки, ул.Комиссара Козявкина, д.4'

    def test_recipient_validate(self):
        rec = BankCardRecipient()

        with self.assertRaises(ValueError):
            rec.validate()

        rec.pof_offer_accepted = True
        with self.assertRaises(ValueError):
            rec.validate()

        rec.skr_destination_card_synonym = 'oALesdd_h_YT6pzpJ10Kn5aB.SC.000.201906'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_first_name = 'Владимир'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_middle_name = 'Владимирович'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_last_name = 'Владимиров'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_doc_number = '4002109067'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_doc_issue_date = '1999-07-30'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_doc_issue_date = datetime.date(1999, 7, 30)
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_address = 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_city = 'Санкт-Петербург'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_country = Currency.RUB
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_postcode = 701152
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_birth_date = '1987-05-24'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_birth_date = datetime.date(1987, 5, 24)
        with self.assertRaises(ValueError):
            rec.validate()

        rec = BankCardRecipient()
        rec.sms_phone_number = '79653457676'
        with self.assertRaises(ValueError):
            rec.validate()

    def test_recipient_map(self):
        rec = BankCardRecipient({
            'pof_offer_accepted': True,
            'skr_destination_card_synonym': 'oALesdd_h_YT6pzpJ10Kn5aB.SC.000.201906',
            'pdr_first_name': 'Владимир',
            'pdr_middle_name': 'Владимирович',
            'pdr_last_name': 'Владимиров',
            'pdr_doc_number': '4002109067',
            'pdr_doc_issue_date': '1999-07-30',
            'pdr_address': 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4',
            'pdr_city': 'Санкт-Петербург',
            'pdr_country': Currency.RUB,
            'pdr_postcode': 701152,
            'pdr_birth_date': '1987-5-24',
            'sms_phone_number': '+79653457676',
        })
        self.assertEqual(rec.map(), {
            "pof_offerAccepted": [str(int(rec.pof_offer_accepted))],
            "skr_destinationCardSynonim": [rec.skr_destination_card_synonym],
            "smsPhoneNumber": [rec.sms_phone_number],
            "pdr_firstName": [rec.pdr_first_name],
            "pdr_middleName": [rec.pdr_middle_name],
            "pdr_lastName": [rec.pdr_last_name],
            "pdr_docNumber": [rec.pdr_doc_number],
            "pdr_docIssueDate": [rec.pdr_doc_issue_date.strftime('%d.%m.%Y')],
            "pdr_postcode": [str(rec.pdr_postcode)],
            "pdr_country": [str(rec.pdr_country)],
            "pdr_city": [rec.pdr_city],
            "pdr_address": [rec.pdr_address],
            "pdr_birthDate": [rec.pdr_birth_date.strftime('%d.%m.%Y')],
        })

        rec = BankCardRecipient({
            'pof_offer_accepted': True,
            'skr_destination_card_synonym': 'oALesdd_h_YT6pzpJ10Kn5aB.SC.000.201906',
            'cps_ym_account': '79653457676',
        })
        self.assertEqual(rec.map(), {
            "pof_offerAccepted": [str(int(rec.pof_offer_accepted))],
            "skr_destinationCardSynonim": [rec.skr_destination_card_synonym],
            'cps_ymAccount': [rec.cps_ym_account],
        })
