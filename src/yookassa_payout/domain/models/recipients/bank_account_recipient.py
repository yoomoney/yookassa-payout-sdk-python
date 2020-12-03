# -*- coding: utf-8 -*-
import datetime
import re

from yookassa_payout.domain.models.recipients.recipient import Recipient


class BankAccountRecipient(Recipient):

    __bank_name = None
    __bank_city = None
    __bank_cor_account = None
    __customer_account = None
    __bank_bik = None
    __payment_purpose = None
    __pdr_first_name = None
    __pdr_middle_name = None
    __pdr_last_name = None
    __pdr_doc_number = None
    __pdr_doc_issue_date = None
    __pdr_address = None
    __pdr_birth_date = None
    __sms_phone_number = None

    @property
    def bank_name(self):
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, value):
        self.__bank_name = str(value)

    @property
    def bank_city(self):
        return self.__bank_city

    @bank_city.setter
    def bank_city(self, value):
        self.__bank_city = str(value)

    @property
    def bank_cor_account(self):
        return self.__bank_cor_account

    @bank_cor_account.setter
    def bank_cor_account(self, value):
        self.__bank_cor_account = str(value)

    @property
    def customer_account(self):
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value):
        self.__customer_account = str(value)

    @property
    def bank_bik(self):
        return self.__bank_bik

    @bank_bik.setter
    def bank_bik(self, value):
        self.__bank_bik = str(value)

    @property
    def payment_purpose(self):
        return self.__payment_purpose

    @payment_purpose.setter
    def payment_purpose(self, value):
        self.__payment_purpose = str(value)

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
                raise ValueError('Invalid pdr_doc_issue_date value')
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
            raise ValueError('Invalid bank_account address value')

    @property
    def pdr_birth_date(self):
        return self.__pdr_birth_date

    @pdr_birth_date.setter
    def pdr_birth_date(self, value):
        if isinstance(value, str):
            try:
                self.__pdr_birth_date = datetime.datetime.strptime(value, '%Y-%m-%d').date()
            except Exception:
                raise ValueError('Invalid pdr_doc_issue_date value')
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
        super(BankAccountRecipient, self).validate()
        if not self.bank_name:
            self.set_validation_error('BankAccountRecipient bank_name not specified')
        if not self.bank_city:
            self.set_validation_error('BankAccountRecipient bank_city not specified')
        if not self.bank_cor_account:
            self.set_validation_error('BankAccountRecipient bank_cor_account not specified')
        if not self.customer_account:
            self.set_validation_error('BankAccountRecipient customer_account not specified')
        if not self.bank_bik:
            self.set_validation_error('BankAccountRecipient bank_bik not specified')
        if not self.payment_purpose:
            self.set_validation_error('BankAccountRecipient payment_purpose not specified')
        if not self.pdr_first_name:
            self.set_validation_error('BankAccountRecipient pdr_first_name not specified')
        if not self.pdr_middle_name:
            self.set_validation_error('BankAccountRecipient pdr_middle_name not specified')
        if not self.pdr_last_name:
            self.set_validation_error('BankAccountRecipient pdr_last_name not specified')
        if not self.pdr_doc_number:
            self.set_validation_error('BankAccountRecipient pdr_doc_number not specified')
        if not self.pdr_doc_issue_date:
            self.set_validation_error('BankAccountRecipient pdr_doc_issue_date not specified')
        if not self.pdr_address:
            self.set_validation_error('BankAccountRecipient pdr_address not specified')
        if not self.pdr_birth_date:
            self.set_validation_error('BankAccountRecipient pdr_birth_date not specified')
        if not self.sms_phone_number:
            self.set_validation_error('BankAccountRecipient sms_phone_number not specified')

    def map(self):
        _map = super(BankAccountRecipient, self).map()
        _map.update({
            "BankName": [self.bank_name],
            "BankCity": [self.bank_city],
            "BankCorAccount": [self.bank_cor_account],
            "CustAccount": [self.customer_account],
            "BankBIK": [self.bank_bik],
            "payment_purpose": [self.payment_purpose],
            "pdr_firstName": [self.pdr_first_name],
            "pdr_middleName": [self.pdr_middle_name],
            "pdr_lastName": [self.pdr_last_name],
            "pdr_docNumber": [self.pdr_doc_number],
            "pdr_docIssueYear": [self.pdr_doc_issue_date.strftime('%Y')],
            "pdr_docIssueMonth": [self.pdr_doc_issue_date.strftime('%m')],
            "pdr_docIssueDay": [self.pdr_doc_issue_date.strftime('%d')],
            "pdr_address": [self.pdr_address],
            "pdr_birthDate": [self.pdr_birth_date.strftime('%d.%m.%Y')],
            "smsPhoneNumber": [self.sms_phone_number],
        })
        return _map
