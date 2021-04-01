# -*- coding: utf-8 -*-
import os
import re
import subprocess
from os.path import abspath
from OpenSSL import crypto

from yookassa_payout.domain.exceptions.open_ssl_error import OpenSSLError


class OpenSSLHelper:
    """
    A helper for work with SSL.
    """
    VERSION_DELIMITER = '/'
    PART_DELIMITER = ' '

    @staticmethod
    def from_file(filename):
        with open(abspath(filename), encoding="utf-8") as f:
            data = f.read()
        return data

    @staticmethod
    def to_file(filename, data):
        with open(abspath(filename), "wb") as f:
            f.write(data)

    @staticmethod
    def encrypt_pkcs7(data, keychain):
        cmd = [
            'openssl', 'smime', '-sign', '-signer', keychain.public_cert, '-inkey', keychain.private_key,
            '-passin', 'pass:' + keychain.key_password, '-nochain', '-nocerts', '-outform', 'PEM', '-nodetach'
        ]

        return OpenSSLHelper.exec_cmd(cmd, data)

    @staticmethod
    def decrypt_pkcs7(data, cert):
        cmd = [
            'openssl', 'smime', '-verify', '-noverify', '-inform', 'PEM', '-nointern',
            '-certfile', cert, '-CAfile', cert
        ]

        return OpenSSLHelper.exec_cmd(cmd, data)

    @staticmethod
    def create_key_pair(key_type, bits):
        """
            Create a public/private key pair.
            Arguments:
              type - Key type, must be one of TYPE_RSA and TYPE_DSA
              bits - Number of bits to use in the key
            Returns: The public/private key pair in a PKey object
       """
        keys = crypto.PKey()
        keys.generate_key(key_type, bits)
        return keys

    @staticmethod
    def create_cert_request(keys, digest="md5", **name):
        """
            Create a certificate request.
            Arguments:
              pkey   - The key to associate with the request
              digest - Digestion method to use for signing, default is md5
              **name - The name of the subject of the request, possible arguments are:
                  C  - Country name
                  ST - State or province name
                  L  - Locality name
                  O  - Organization name
                  OU - Organizational unit name
                  CN - Common name
                  emailAddress - E-mail address
            Returns: The certificate request in an X509Req object
       """
        req = crypto.X509Req()
        subj = req.get_subject()

        for (key, value) in name.items():
            setattr(subj, key, value)

        req.set_pubkey(keys)
        req.sign(keys, digest)
        return req

    @staticmethod
    def create_certificate(req, issuer_cert_key, serial, validity_period, digest="sha256"):
        """
            Generate a certificate given a certificate request.
            Arguments:
                req         - Certificate request to use
                issuer_cert - The certificate of the issuer
                issuer_key  - The private key of the issuer
                serial      - Serial number for the certificate
                not_before  - Timestamp (relative to now) when the certificate starts being valid
                not_after   - Timestamp (relative to now) when the certificate stops being valid
                digest      - Digest method to use for signing, default is sha256
            Returns: The signed certificate in an X509 object
        """
        issuer_cert, issuer_key = issuer_cert_key
        not_before, not_after = validity_period
        cert = crypto.X509()
        cert.set_serial_number(serial)
        cert.gmtime_adj_notBefore(not_before)
        cert.gmtime_adj_notAfter(not_after)
        cert.set_issuer(issuer_cert.get_subject())
        cert.set_subject(req.get_subject())
        cert.set_pubkey(req.get_pubkey())
        cert.sign(issuer_key, digest)
        return cert

    @staticmethod
    def create_signature(req_file):
        output = OpenSSLHelper.exec_cmd(['openssl', 'req', '-in', req_file, '-noout', '-text'], '')
        match_obj = re.search(r'Signature Algorithm: (.*)', output.decode(), re.M | re.I | re.S | re.A)
        if match_obj:
            sign_lines = match_obj.group(1).split('         ')
            sign_lines.pop(0)
            signature = ''.join(sign_lines)
        else:
            signature = None

        return signature

    """"""

    @staticmethod
    def exec_cmd(cmd, data):
        r"""
        :param cmd: list
        :param data: str
        :return: str
        """

        output = None
        read, write = os.pipe()
        os.write(write, data.encode("utf-8"))
        os.close(write)

        try:
            output = subprocess.check_output(cmd, stdin=read, timeout=5, stderr=subprocess.STDOUT)
        except subprocess.TimeoutExpired:
            raise OpenSSLError("Timeout when running:\n{}".format(' '.join(cmd)))
        except subprocess.CalledProcessError as e:
            raise OpenSSLError("Error {} - {}".format(e.returncode, e.output.decode("utf-8")))
        except subprocess.SubprocessError as e:
            raise OpenSSLError("Error when running:\n{}".format(', '.join(e.args)))

        return output
