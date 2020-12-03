# -*- coding: utf-8 -*-
import unittest
import datetime

from yookassa_payout.domain.models.recipients.bank_account_recipient import BankAccountRecipient


class TestBankAccountRecipient(unittest.TestCase):

    def test_recipient_cast(self):
        rec = BankAccountRecipient()
        rec.pof_offer_accepted = True
        rec.bank_name = 'ПАО Сбербанк'
        rec.bank_city = 'г.Москва'
        rec.bank_cor_account = '30101810400000000225'
        rec.customer_account = '40817810255030943620'
        rec.bank_bik = '042809679'
        rec.payment_purpose = 'Возврат по договору 25-001, без НДС'
        rec.pdr_first_name = 'Владимир'
        rec.pdr_middle_name = 'Владимирович'
        rec.pdr_last_name = 'Владимиров'
        rec.pdr_doc_number = '4002109067'
        rec.pdr_doc_issue_date = '1999-07-30'
        rec.pdr_address = 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4'
        rec.pdr_birth_date = '1987-05-24'
        rec.sms_phone_number = '79653457676'

        self.assertEqual({
            'pof_offer_accepted': True,
            'bank_name': 'ПАО Сбербанк',
            'bank_city': 'г.Москва',
            'bank_cor_account': '30101810400000000225',
            'customer_account': '40817810255030943620',
            'bank_bik': '042809679',
            'payment_purpose': 'Возврат по договору 25-001, без НДС',
            'pdr_first_name': 'Владимир',
            'pdr_middle_name': 'Владимирович',
            'pdr_last_name': 'Владимиров',
            'pdr_doc_number': '4002109067',
            'pdr_doc_issue_date': datetime.date(1999, 7, 30),
            'pdr_address': 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4',
            'pdr_birth_date': datetime.date(1987, 5, 24),
            'sms_phone_number': '79653457676',
        }, dict(rec))

    def test_recipient_setters(self):
        rec = BankAccountRecipient({
            'pof_offer_accepted': True,
            'bank_name': 'ПАО Сбербанк',
            'bank_city': 'г.Москва',
            'bank_cor_account': '30101810400000000225',
            'customer_account': '40817810255030943620',
            'bank_bik': '042809679',
            'payment_purpose': 'Возврат по договору 25-001, без НДС',
            'pdr_first_name': 'Владимир',
            'pdr_middle_name': 'Владимирович',
            'pdr_last_name': 'Владимиров',
            'pdr_doc_number': '4002109067',
            'pdr_doc_issue_date': '1999-07-30',
            'pdr_address': 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4',
            'pdr_birth_date': '1987-5-24',
            'sms_phone_number': '+79653457676',
        })

        self.assertIsInstance(rec.pof_offer_accepted, bool)
        self.assertEqual(rec.pof_offer_accepted, True)

        self.assertIsInstance(rec.bank_name, str)
        self.assertEqual(rec.bank_name, 'ПАО Сбербанк')

        self.assertIsInstance(rec.bank_city, str)
        self.assertEqual(rec.bank_city, 'г.Москва')

        self.assertIsInstance(rec.bank_cor_account, str)
        self.assertEqual(rec.bank_cor_account, '30101810400000000225')

        self.assertIsInstance(rec.customer_account, str)
        self.assertEqual(rec.customer_account, '40817810255030943620')

        self.assertIsInstance(rec.bank_bik, str)
        self.assertEqual(rec.bank_bik, '042809679')

        self.assertIsInstance(rec.payment_purpose, str)
        self.assertEqual(rec.payment_purpose, 'Возврат по договору 25-001, без НДС')

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
        rec = BankAccountRecipient()

        with self.assertRaises(ValueError):
            rec.validate()

        rec.pof_offer_accepted = True
        with self.assertRaises(ValueError):
            rec.validate()

        rec.bank_name = 'ПАО Сбербанк'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.bank_city = 'г.Москва'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.bank_cor_account = '30101810400000000225'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.customer_account = '40817810255030943620'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.bank_bik = '042809679'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.payment_purpose = 'Возврат по договору 25-001, без НДС'
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

        rec.pdr_address = 123456
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_birth_date = '1987-05-24'
        with self.assertRaises(ValueError):
            rec.validate()

        rec.pdr_birth_date = datetime.date(1987, 5, 24)
        with self.assertRaises(ValueError):
            rec.validate()

        rec = BankAccountRecipient()
        rec.sms_phone_number = '79653457676'
        with self.assertRaises(ValueError):
            rec.validate()

    def test_recipient_map(self):
        rec = BankAccountRecipient({
            'pof_offer_accepted': True,
            'bank_name': 'ПАО Сбербанк',
            'bank_city': 'г.Москва',
            'bank_cor_account': '30101810400000000225',
            'customer_account': '40817810255030943620',
            'bank_bik': '042809679',
            'payment_purpose': 'Возврат по договору 25-001, без НДС',
            'pdr_first_name': 'Владимир',
            'pdr_middle_name': 'Владимирович',
            'pdr_last_name': 'Владимиров',
            'pdr_doc_number': '4002109067',
            'pdr_doc_issue_date': '1999-07-30',
            'pdr_address': 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4',
            'pdr_birth_date': '1987-5-24',
            'sms_phone_number': '+79653457676',
        })
        self.assertEqual(rec.map(), {
            "pof_offerAccepted": [str(int(rec.pof_offer_accepted))],
            "BankName": [rec.bank_name],
            "BankCity": [rec.bank_city],
            "BankCorAccount": [rec.bank_cor_account],
            "CustAccount": [rec.customer_account],
            "BankBIK": [rec.bank_bik],
            "payment_purpose": [rec.payment_purpose],
            "pdr_firstName": [rec.pdr_first_name],
            "pdr_middleName": [rec.pdr_middle_name],
            "pdr_lastName": [rec.pdr_last_name],
            "pdr_docNumber": [rec.pdr_doc_number],
            "pdr_docIssueYear": [rec.pdr_doc_issue_date.strftime('%Y')],
            "pdr_docIssueMonth": [rec.pdr_doc_issue_date.strftime('%m')],
            "pdr_docIssueDay": [rec.pdr_doc_issue_date.strftime('%d')],
            "pdr_address": [rec.pdr_address],
            "pdr_birthDate": [rec.pdr_birth_date.strftime('%d.%m.%Y')],
            "smsPhoneNumber": [rec.sms_phone_number],
        })
