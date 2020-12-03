# -*- coding: utf-8 -*-
import logging
import logging.config
import sys
import time
import unittest

from yookassa_payout.configuration import Configuration, ConfigurationError
from yookassa_payout.domain.common.keychain import KeyChain
from yookassa_payout.logging.adapter import Adapter


class TestConfiguration(unittest.TestCase):

    def test_configuration(self):
        tz = time.strftime('%z')
        logging.config.dictConfig({
            "version": 1,
            "handlers": {
                "streamHandler": {
                    "class": "logging.StreamHandler",
                    "formatter": "appFormatter",
                    "stream": sys.stdout
                },
                "hekaHandler": {
                    "class": "logging.FileHandler",
                    "formatter": "hekaFormatter",
                    "filename": "heka.log"
                },
                "jsonHandler": {
                    "class": "logging.FileHandler",
                    "formatter": "jsonFormatter",
                    "filename": "json.log"
                }
            },
            "loggers": {
                "app": {
                    "handlers": ["streamHandler", "jsonHandler"],
                    "level": "DEBUG",
                },
                "heka": {
                    "handlers": ["streamHandler", "hekaHandler"],
                    "level": "DEBUG",
                }
            },
            "formatters": {
                "appFormatter": {
                    "format": "[%(asctime)s.%(msecs)03d" + tz + "] %(levelname)s [ ] [%(name)s] %(message)s",
                    "datefmt": "%Y-%m-%dT%H:%M:%S"
                },
                "jsonFormatter": {
                    "format": '{'
                              '"message": "%(message)s", "level": "%(levelname)s", "channel": "%(name)s", '
                              '"extra": [], "app_name": "wix", "app_type": "php", "log_type": "code", '
                              '"es_index_name": "php-wix-main", "timestamp": "%(asctime)s.%(msecs)03d' + tz + '"'
                              '}',
                    "datefmt": "%Y-%m-%dT%H:%M:%S"
                },
                "hekaFormatter": {
                    "format": "{}.all.{}.{}.%(message)s:{}".format("dc", "prefix", "type", "postfix"),
                }
            }
        })

        log = logging.getLogger('app')
        heka = logging.getLogger('heka')
        keychain = KeyChain('public_cert', 'private_key', 'key_password')
        Configuration.configure(250000, keychain, log)
        configuration = Configuration.instantiate()

        self.assertEqual(configuration.agent_id, 250000)
        self.assertEqual(configuration.timeout, 1800)
        self.assertEqual(configuration.max_attempts, 3)
        # var_dump(dict(configuration))
        self.assertIsInstance(configuration.logger, Adapter)
        heka.debug('test')
