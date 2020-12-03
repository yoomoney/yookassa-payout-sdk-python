# -*- coding: utf-8 -*-
import datetime
import unittest
import uuid

from dateutil import tz

from yookassa_payout.domain.common.currency import Currency
from yookassa_payout.domain.models.recipients.recipient import Recipient
from yookassa_payout.domain.request.make_deposition_request import MakeDepositionRequest


class TestMakeDepositionRequest(unittest.TestCase):

    def test_request_cast(self):
        request = MakeDepositionRequest()
        request.agent_id = 250000
        request.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        request.request_dt = '2020-03-04T15:39:45.456+03:00'

        rec = Recipient()
        rec.pof_offer_accepted = True
        request.payment_params = rec

        self.assertEqual({
            'agent_id': 250000,
            'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            'request_dt': datetime.datetime(2020, 3, 4, 15, 39, 45, 456000, tzinfo=tz.gettz('Europe/Moscow')),
            'request_name': 'makeDeposition',
            'payment_params': {'pof_offer_accepted': True},
        }, dict(request))

    def test_request_setters(self):
        request = MakeDepositionRequest(self.create_make_params())

        self.assertIsInstance(request.agent_id, int)
        self.assertIsInstance(request.request_dt, datetime.datetime)
        self.assertEqual(request.request_name, 'makeDeposition')
        self.assertIsInstance(request.payment_params, Recipient)
        self.assertIsInstance(request.payment_params.pof_offer_accepted, bool)

        with self.assertRaises(ValueError):
            request.request_dt = 'invalid request_dt'

        with self.assertRaises(TypeError):
            request.request_dt = object()

        with self.assertRaises(TypeError):
            request.payment_params = 'invalid payment_params'

    def test_request_validate(self):
        request = MakeDepositionRequest()

        with self.assertRaises(ValueError):
            request.validate()

        request.agent_id = 250000
        with self.assertRaises(ValueError):
            request.validate()

        request.agent_id = 0
        request.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        with self.assertRaises(ValueError):
            request.validate()

        request.agent_id = 250000
        request.client_order_id = ''
        with self.assertRaises(ValueError):
            request.validate()

        request.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'

        with self.assertRaises(ValueError):
            request.payment_params = {'invalid': 1}

        with self.assertRaises(ValueError):
            request.validate()

        request = MakeDepositionRequest()
        request.payment_params = Recipient({'pof_offer_accepted': True})
        with self.assertRaises(ValueError):
            request.validate()

        request = MakeDepositionRequest()
        request.payment_params = Recipient({'pof_offer_accepted': True})
        request.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
        with self.assertRaises(ValueError):
            request.validate()

        request = MakeDepositionRequest()
        request.payment_params = Recipient({'pof_offer_accepted': True})
        request.agent_id = 250000
        with self.assertRaises(ValueError):
            request.validate()

    def test_request_map(self):
        req = MakeDepositionRequest(self.create_make_params())
        self.assertEqual(req.map(), {
            'makeDepositionRequest': {
                "requestDT": req.request_dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
                "agentId": req.agent_id,
                "clientOrderId": req.client_order_id,
                "dstAccount": req.dst_account,
                "amount": format(req.amount, ".2f"),
                "currency": req.currency,
                "contract": req.contract,
                "paymentParams": {
                    "pof_offerAccepted": ['1'],
                    "skr_destinationCardSynonim": [req.payment_params.skr_destination_card_synonym],
                    "smsPhoneNumber": [req.payment_params.sms_phone_number],
                    "pdr_firstName": [req.payment_params.pdr_first_name],
                    "pdr_middleName": [req.payment_params.pdr_middle_name],
                    "pdr_lastName": [req.payment_params.pdr_last_name],
                    "pdr_docNumber": [req.payment_params.pdr_doc_number],
                    "pdr_docIssueDate": [req.payment_params.pdr_doc_issue_date.strftime('%d.%m.%Y')],
                    "pdr_postcode": [str(req.payment_params.pdr_postcode)],
                    "pdr_country": [str(req.payment_params.pdr_country)],
                    "pdr_city": [req.payment_params.pdr_city],
                    "pdr_address": [req.payment_params.pdr_address],
                    "pdr_birthDate": [req.payment_params.pdr_birth_date.strftime('%d.%m.%Y')],
                }
            }
        })

    @staticmethod
    def create_make_params():
        client_order_id = str(uuid.uuid4())
        return {
            "agent_id": 250000,
            "client_order_id": client_order_id,
            "dst_account": "41001614575714",
            "amount": 10.00,
            "currency": Currency.RUB,
            "contract": "Зачисление на кошелек",
            "payment_params": {
                "skr_destination_card_synonym": "h4h8FWCnhpiGKrg5eRKQ6hQS.SC.000.202003",
                "pof_offer_accepted": True,
                "sms_phone_number": "79818932328",
                "pdr_first_name": "Эдуард",
                "pdr_last_name": "Запеканкин",
                "pdr_doc_number": "1013123456",
                "pdr_doc_issue_date": "2013-10-10",
                "pdr_country": Currency.RUB,
                "pdr_birth_date": "1973-10-31"
            }
        }
