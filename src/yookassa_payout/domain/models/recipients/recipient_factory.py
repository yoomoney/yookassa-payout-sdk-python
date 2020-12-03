# -*- coding: utf-8 -*-
from yookassa_payout.domain.models.recipients.bank_account_recipient import BankAccountRecipient
from yookassa_payout.domain.models.recipients.bank_card_recipient import BankCardRecipient
from yookassa_payout.domain.models.recipients.recipient import Recipient


class RecipientFactory(object):

    @staticmethod
    def factory(data):
        if isinstance(data, dict):
            if 'customer_account' in data:
                return BankAccountRecipient(data)
            elif 'skr_destination_card_synonym' in data:
                return BankCardRecipient(data)
            elif 'pof_offer_accepted' in data:
                return Recipient(data)
            else:
                raise ValueError('Invalid recipient_factory value')
        else:
            raise TypeError('Invalid recipient_factory value type')
