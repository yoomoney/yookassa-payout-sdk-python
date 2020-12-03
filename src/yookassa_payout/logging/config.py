# -*- coding: utf-8 -*-
import json
import sys
import time


class Formatters:
    __tz = time.strftime('%z')

    APP = {
        "name": "appFormatter",
        "config": {
            "format": "[%(asctime)s.%(msecs)03d" + __tz + "] %(levelname)s [ ] [%(name)s] %(message)s %(context)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        }
    }
    JSON = {
        "name": "jsonFormatter",
        "config": {
            "format": json.dumps({
                "message": "%(message)s", "level": "%(levelname)s", "channel": "%(name)s",
                "extra": [], "app_name": "app_main", "app_type": "python", "log_type": "code",
                "es_index_name": "python-main", "timestamp": "%(asctime)s.%(msecs)03d" + __tz,
                "context": "%(context)s"
            }),
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        }
    }
    HEKA = {
        "name": "hekaFormatter",
        "config": {"format": "{}.all.{}.{}.%(message)s:{}".format("dc", "prefix", "type", "postfix")}
    }


class Handlers:
    STREAM = {
        "name": "streamHandler",
        "config": {"class": "logging.StreamHandler", "formatter": Formatters.APP['name'], "stream": sys.stdout}
    }
    JSON = {
        "name": "jsonHandler",
        "config": {"class": "logging.FileHandler", "formatter": Formatters.JSON['name'], "filename": "json.log"}
    }
    HEKA = {
        "name": "hekaHandler",
        "config": {"class": "logging.FileHandler", "formatter": Formatters.HEKA['name'], "filename": "heka.log"}
    }


class Loggers:
    APP = {
        "name": "app",
        "config": {"handlers": [Handlers.STREAM['name'], Handlers.JSON['name']], "level": "DEBUG"}
    }
    HEKA = {
        "name": "heka",
        "config": {"handlers": [Handlers.HEKA['name']], "level": "DEBUG"}  # Handlers.STREAM['name'],
    }
