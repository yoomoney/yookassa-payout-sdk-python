# -*- coding: utf-8 -*-
from yookassa_payout.domain.common.base_object import BaseObject


class Recipient(BaseObject):

    __pof_offer_accepted = None

    @property
    def pof_offer_accepted(self):
        return self.__pof_offer_accepted

    @pof_offer_accepted.setter
    def pof_offer_accepted(self, value):
        if isinstance(value, bool):
            self.__pof_offer_accepted = value
        else:
            raise ValueError('Invalid pof_offer_accepted value')

    def validate(self):
        if not self.pof_offer_accepted:
            self.set_validation_error('Recipient pof_offer_accepted not specified')

    def set_validation_error(self, message):
        raise ValueError(message)

    def map(self):
        self.validate()
        return {
            "pof_offerAccepted": [str(int(self.pof_offer_accepted))]
        }
