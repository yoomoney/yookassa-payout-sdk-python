# -*- coding: utf-8 -*-
"""Main module."""
import uuid
from os.path import abspath

from yookassa_payout.domain.common.client import ApiClient
from yookassa_payout.domain.common.generator_csr import GeneratorCsr
from yookassa_payout.domain.exceptions.api_error import ApiError
from yookassa_payout.domain.request.balance_request import BalanceRequest
from yookassa_payout.domain.request.deposition_request import DepositionRequest
from yookassa_payout.domain.request.deposition_request_builder import DepositionRequestBuilder
from yookassa_payout.domain.request.synonym_card_request import SynonymCardRequest
from yookassa_payout.domain.response.balance_response import BalanceResponse
from yookassa_payout.domain.response.deposition_response_builder import DepositionResponseBuilder
from yookassa_payout.domain.response.synonym_card_response import SynonymCardResponse


class Payout(object):
    """
    YooKassaPayout Class
    """
    def __init__(self):
        self.client = ApiClient()
        self.agent_id = self.client.configuration.agent_id

    @classmethod
    def get_balance(cls, client_order_id=None):
        """
        Get Balance Method

        # Arguments
        client_order_id (str, None):

        # Raises
        ApiError: If *client_order_id* does unsupported format

        # Returns
        BalanceResponse: Data
        """
        instance = cls()
        path = instance.client.BALANCE_REQUEST

        if not client_order_id:
            client_order_id = uuid.uuid4()

        request = BalanceRequest({"agent_id": instance.agent_id, "client_order_id": client_order_id})
        response = instance.client.request(path, request)

        if response and 'balanceResponse' in response:
            return BalanceResponse(response['balanceResponse'])
        else:
            raise ApiError('Cannot get data!')

    @classmethod
    def get_synonym_card(cls, data):
        """
        Get Synonym Card Method

        # Arguments
        data (SynonymCardRequest, dict): SynonymCard data

        # Raises
        ValueError: If *params* does unsupported format data

        # Returns
        SynonymCardResponse:
        """
        instance = cls()
        path = instance.client.SYNONYM_CARD_REQUEST

        if isinstance(data, dict):
            request = SynonymCardRequest(data)
        elif isinstance(data, SynonymCardRequest):
            request = data
        else:
            raise ApiError('Unsupported data format!')

        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        response = instance.client.request(path, request, headers=headers, is_ssl=False)

        if response and 'storeCard' in response:
            return SynonymCardResponse(response['storeCard'])
        else:
            raise ApiError('Cannot get data!')

    @classmethod
    def create_deposition(cls, data):
        """
        Create Deposition

        # Arguments
        data (DepositionRequest, data):

        # Raises
        ApiError: If *data* does unsupported format data
        ValueError: If *data* does unsupported format data

        # Returns
        MakeDepositionResponse | TestDepositionResponse: Data
        """
        instance = cls()
        path = instance.client.DEPOSITION_REQUEST

        if isinstance(data, dict):
            request = DepositionRequestBuilder.build(data)
        elif isinstance(data, DepositionRequest):
            request = data
        else:
            raise ApiError('Unsupported data format!')

        request.validate()

        response = instance.client.request(path.format(request.request_name), request)
        return DepositionResponseBuilder.build(response)

    @staticmethod
    def get_csr(org, output, key_pass):
        gen = GeneratorCsr(key_pass, org, abspath(output))
        gen.generate_all()
