# -*- coding: utf-8 -*-
import datetime
import re

from yookassa_payout.domain.models.recipients.recipient import Recipient


class BankCardRecipient(Recipient):

    __skr_destination_card_synonym = None
    __cps_ym_account = None
    __pdr_first_name = None
    __pdr_middle_name = None
    __pdr_last_name = None
    __pdr_doc_number = None
    __pdr_doc_issue_date = None
    __pdr_address = None
    __pdr_country = None
    __pdr_city = None
    __pdr_postcode = None
    __pdr_birth_date = None
    __sms_phone_number = None

    @property
    def skr_destination_card_synonym(self):
        return self.__skr_destination_card_synonym

    @skr_destination_card_synonym.setter
    def skr_destination_card_synonym(self, value):
        self.__skr_destination_card_synonym = str(value)

    @property
    def cps_ym_account(self):
        return self.__cps_ym_account

    @cps_ym_account.setter
    def cps_ym_account(self, value):
        self.__cps_ym_account = str(value)

    @property
    def pdr_first_name(self):
        return self.__pdr_first_name

    @pdr_first_name.setter
    def pdr_first_name(self, value):
        self.__pdr_first_name = str(value)

    @property
    def pdr_middle_name(self):
        return self.__pdr_middle_name

    @pdr_middle_name.setter
    def pdr_middle_name(self, value):
        self.__pdr_middle_name = str(value)

    @property
    def pdr_last_name(self):
        return self.__pdr_last_name

    @pdr_last_name.setter
    def pdr_last_name(self, value):
        self.__pdr_last_name = str(value)

    @property
    def pdr_doc_number(self):
        return self.__pdr_doc_number

    @pdr_doc_number.setter
    def pdr_doc_number(self, value):
        self.__pdr_doc_number = str(value)

    @property
    def pdr_doc_issue_date(self):
        return self.__pdr_doc_issue_date

    @pdr_doc_issue_date.setter
    def pdr_doc_issue_date(self, value):
        if isinstance(value, str):
            try:
                self.__pdr_doc_issue_date = datetime.datetime.strptime(value, '%Y-%m-%d').date()
            except Exception:
                raise ValueError('Invalid pdr_doc_issue_date value type')
        elif isinstance(value, datetime.date):
            self.__pdr_doc_issue_date = value
        else:
            raise TypeError('Invalid pdr_doc_issue_date value type')

    @property
    def pdr_address(self):
        return self.__pdr_address

    @pdr_address.setter
    def pdr_address(self, value):
        cast_value = str(value)
        if cast_value and len(cast_value) <= 100:
            self.__pdr_address = cast_value
        else:
            raise ValueError('Invalid pdr_address value')

    @property
    def pdr_city(self):
        return self.__pdr_city

    @pdr_city.setter
    def pdr_city(self, value):
        self.__pdr_city = str(value)

    @property
    def pdr_country(self):
        return self.__pdr_country

    @pdr_country.setter
    def pdr_country(self, value):
        self.__pdr_country = int(value)

    @property
    def pdr_postcode(self):
        return self.__pdr_postcode

    @pdr_postcode.setter
    def pdr_postcode(self, value):
        self.__pdr_postcode = int(value)

    @property
    def pdr_birth_date(self):
        return self.__pdr_birth_date

    @pdr_birth_date.setter
    def pdr_birth_date(self, value):
        if isinstance(value, str):
            try:
                self.__pdr_birth_date = datetime.datetime.strptime(value, '%Y-%m-%d').date()
            except Exception:
                raise ValueError('Invalid pdr_doc_issue_date value type')
        elif isinstance(value, datetime.date):
            self.__pdr_birth_date = value
        else:
            raise TypeError('Invalid pdr_doc_issue_date value type')

    @property
    def sms_phone_number(self):
        return self.__sms_phone_number

    @sms_phone_number.setter
    def sms_phone_number(self, value):
        cast_value = re.sub(r'[^\d]', '', str(value))
        if re.match('^[0-9]{4,15}$', cast_value):
            self.__sms_phone_number = cast_value
        else:
            raise ValueError('Invalid phone value type')

    def validate(self):
        super(BankCardRecipient, self).validate()

        if not self.skr_destination_card_synonym:
            self.set_validation_error('BankCardRecipient skr_destination_card_synonym not specified')

        if not self.cps_ym_account:
            if not self.pdr_first_name:
                self.set_validation_error('BankCardRecipient pdr_first_name not specified')
            if not self.pdr_last_name:
                self.set_validation_error('BankCardRecipient pdr_last_name not specified')
            if not self.pdr_doc_number:
                self.set_validation_error('BankCardRecipient pdr_doc_number not specified')
            if not self.pdr_doc_issue_date:
                self.set_validation_error('BankCardRecipient pdr_doc_issue_date not specified')
            if not self.pdr_country:
                self.set_validation_error('BankCardRecipient pdr_country not specified')
            if not self.pdr_birth_date:
                self.set_validation_error('BankCardRecipient pdr_birth_date not specified')
            if not self.sms_phone_number:
                self.set_validation_error('BankCardRecipient sms_phone_number not specified')

    def map(self):
        _map = super(BankCardRecipient, self).map()

        if self.cps_ym_account:
            _map.update({
                "skr_destinationCardSynonim": [self.skr_destination_card_synonym],
                "cps_ymAccount": [self.cps_ym_account],
            })
        else:
            _map.update({
                "skr_destinationCardSynonim": [self.skr_destination_card_synonym],
                "smsPhoneNumber": [self.sms_phone_number],
                "pdr_firstName": [self.pdr_first_name],
                "pdr_middleName": [self.pdr_middle_name],
                "pdr_lastName": [self.pdr_last_name],
                "pdr_docNumber": [self.pdr_doc_number],
                "pdr_docIssueDate": [self.pdr_doc_issue_date.strftime('%d.%m.%Y')],
                "pdr_postcode": [str(self.pdr_postcode)],
                "pdr_country": [str(self.pdr_country)],
                "pdr_city": [self.pdr_city],
                "pdr_address": [self.pdr_address],
                "pdr_birthDate": [self.pdr_birth_date.strftime('%d.%m.%Y')],
            })

        return _map
