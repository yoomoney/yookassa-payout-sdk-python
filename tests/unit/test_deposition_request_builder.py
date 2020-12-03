# -*- coding: utf-8 -*-
import unittest

from yookassa_payout.domain.exceptions.api_error import ApiError
from yookassa_payout.domain.request.deposition_request_builder import DepositionRequestBuilder
from yookassa_payout.domain.request.make_deposition_request import MakeDepositionRequest
from yookassa_payout.domain.request.test_deposition_request import TestDepositionRequest as TDepositionRequest


class TestDepositionRequestBuilder(unittest.TestCase):

    def test_build(self):
        req = DepositionRequestBuilder.build({
            'testDeposition': {
                'agent_id': 250000,
                'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
            }
        })

        self.assertIsInstance(req, TDepositionRequest)
        self.assertEqual(req.request_name, 'testDeposition')
        self.assertEqual(req.agent_id, 250000)
        self.assertEqual(req.client_order_id, '215d8da0-000f-50be-b000-0003308c89be')

        req = DepositionRequestBuilder.build({
            'makeDeposition': {
                'agent_id': 250000,
                'client_order_id': '215d8da0-000f-50be-b000-0003308c89be',
                'request_name': 'makeDeposition',
                'payment_params': {'pof_offer_accepted': True},
            }
        })

        self.assertIsInstance(req, MakeDepositionRequest)
        self.assertEqual(req.request_name, 'makeDeposition')
        self.assertEqual(req.agent_id, 250000)
        self.assertEqual(req.client_order_id, '215d8da0-000f-50be-b000-0003308c89be')
        self.assertEqual(req.payment_params.pof_offer_accepted, True)

        with self.assertRaises(ApiError):
            req = DepositionRequestBuilder.build({
                'fakeDeposition': {}
            })
