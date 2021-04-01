# -*- coding: utf-8 -*-
import os

from OpenSSL import crypto
from yookassa_payout.domain.common.openssl_helper import OpenSSLHelper
from yookassa_payout.domain.models.organization import Organization


class GeneratorCsr:
    """
    A helper for generate cert.
    """

    FILE_KEY = 'private_key.pem'
    FILE_CRT = 'client_cert.crt'
    FILE_CSR = 'request.csr'
    FILE_SIG = 'signature.txt'

    __key_password = None
    __organization = None
    __output_dir = None

    def __init__(self, private_key_password, organization_info, output_dir):
        self.key_password = private_key_password
        self.organization = organization_info
        self.output_dir = output_dir

    def generate_all(self):
        self.generate()
        return

    def generate_csr_with_private_key(self, key_path):
        self.generate(key_path)
        return

    def generate(self, key_path=None):
        if key_path is not None:
            ca_key = crypto.load_privatekey(
                crypto.FILETYPE_PEM, OpenSSLHelper.from_file(key_path),
                self.key_password.encode('utf-8')
            )
        else:
            ca_key = OpenSSLHelper.create_key_pair(crypto.TYPE_RSA, 2048)

        ca_req = OpenSSLHelper.create_cert_request(ca_key,
                                                   C=self.organization.country_name,
                                                   ST=self.organization.state,
                                                   L=self.organization.locality,
                                                   O=self.organization.org_name,
                                                   OU=self.organization.org_unit_name,
                                                   CN=self.organization.common_name,
                                                   emailAddress=self.organization.email)
        ca_cert = OpenSSLHelper.create_certificate(ca_req, (ca_req, ca_key), 123456789, (0, 60 * 60 * 24 * 365))

        if key_path is None:
            dump_private_key = crypto.dump_privatekey(
                crypto.FILETYPE_PEM, ca_key, 'aes256', self.key_password.encode('utf-8')
            )
            OpenSSLHelper.to_file(self.output_dir + os.path.sep + self.FILE_KEY, dump_private_key)

        dump_certificate = crypto.dump_certificate(crypto.FILETYPE_PEM, ca_cert)
        OpenSSLHelper.to_file(self.output_dir + os.path.sep + self.FILE_CRT, dump_certificate)

        dump_certificate_request = crypto.dump_certificate_request(crypto.FILETYPE_PEM, ca_req)
        OpenSSLHelper.to_file(self.output_dir + os.path.sep + self.FILE_CSR, dump_certificate_request)

        signature = OpenSSLHelper.create_signature(self.output_dir + os.path.sep + self.FILE_CSR)
        OpenSSLHelper.to_file(self.output_dir + os.path.sep + self.FILE_SIG, signature.encode('utf-8'))

        return

    @property
    def key_password(self):
        return self.__key_password

    @key_password.setter
    def key_password(self, value):
        self.__key_password = str(value)

    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, value):
        if isinstance(value, dict):
            self.__organization = Organization(value)
        elif isinstance(value, Organization):
            self.__organization = value
        else:
            raise TypeError('Invalid organization value type')

        if not self.__organization.verify():
            raise ValueError('Fields common_name, email, org_name, country_name and state are required.')

    @property
    def output_dir(self):
        return self.__output_dir

    @output_dir.setter
    def output_dir(self, value):
        if not os.path.exists(value):
            os.makedirs(value)
        self.__output_dir = value

    def get_file_list(self):
        ret = {}
        for ftype in ['FILE_KEY', 'FILE_CRT', 'FILE_CSR', 'FILE_SIG']:
            path = self.output_dir + os.path.sep + getattr(self, ftype)
            ret.update({ftype: {'path': path, 'exist': os.path.exists(path)}})

        return ret
