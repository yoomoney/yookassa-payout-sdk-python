# -*- coding: utf-8 -*-
import os
from getpass import getpass
from os.path import abspath

from yookassa_payout.domain.common.generator_csr import GeneratorCsr
from yookassa_payout.domain.models.organization import Organization


class CliClient:

    org_fields = {
        'country_name': {'name': 'Страна', 'hint': '2-х буквенный код', 'req': True, 'default': 'RU', },
        'state': {'name': 'Страна или Штат', 'hint': 'полное название', 'req': True, 'default': 'Russia', },
        'locality': {'name': 'Населенный пункт', 'hint': 'например, город', 'req': False, 'default': None, },
        'org_name': {'name': 'Название организации', 'hint': 'например, компания', 'req': True, 'default': None, },
        'org_unit_name': {'name': 'Название подразделения', 'hint': 'например, отдел', 'req': False, 'default': None, },
        'common_name': {'name': 'Основное название', 'hint': 'например, имякомпании', 'req': True, 'default': None, },
        'email': {'name': 'Email адрес', 'hint': None, 'req': True, 'default': None, },
    }

    def generate(self, key_path=None):
        org = self.fill_org()
        output = self.fill_output(key_path)
        password = self.fill_password()
        self.print_data(org, output)
        self.run_generator(password, org, output, key_path)

    def print_data(self, org, output):
        ret = C.c(C.CYELLOW2, "\nВаши данные:\n")
        for name, item in self.org_fields.items():
            attr = getattr(org, name)
            ret += "{}: {}\n".format(item['name'], C.c(C.CRED2, '-') if attr == '' else C.c(C.CGREEN2, attr))
        ret += "Каталог для генерации файлов: {}\n".format(C.c(C.CGREEN2, output))
        print(ret)

    def fill_org(self):
        org = Organization()
        for name, item in self.org_fields.items():
            successful = False
            while not successful:
                prompt = "{}{} [{}{}]: ".format(
                    item['name'],
                    '' if item['hint'] is None else " (" + item['hint'] + ")",
                    '' if item['default'] is None else str(item['default']),
                    '' if not item['req'] else C.c(C.CRED2, '*'),
                )
                print(prompt)

                while True:
                    val = input()
                    if item['default'] and not val:
                        val = item['default']

                    if item['req'] and not val:
                        print(C.c(C.CRED2, "Ошибка! `{}` не может быть пустым!".format(item['name'])))
                        print(prompt)
                    else:
                        break

                if item['default'] and not val:
                    val = item['default']

                try:
                    setattr(org, name, val)
                    successful = True
                except ValueError as e:
                    print(C.c(C.CRED2, "Ошибка! {}".format(str(e))))

        return org

    def fill_output(self, key_path=None):
        default = os.getcwd()

        prompt = "Введите каталог для "
        if key_path is None:
            prompt += "privateKey и "
        prompt += "request.csr [{}]: "

        print(prompt.format(default))
        val = input()

        return default if not val else str(val)

    def fill_password(self):
        prompt = "Введите пароль для приватного ключа {}: ".format(C.c(C.CRED2, '*'))
        print(prompt)
        while True:
            val = getpass()
            if not val:
                print(C.c(C.CRED2, "Ошибка! Пароль не может быть пустым!"))
                print(prompt)
            else:
                break

        return str(val)

    def run_generator(self, password, org, output, key_path=None):
        default = "no"
        prompt = "Вы готовы сгенерировать файлы? (yes|no) [{}]: ".format(default)
        print(prompt)
        val = input()

        if val == 'yes':
            gen = GeneratorCsr(password, org, abspath(output))
            if key_path is not None:
                gen.generate_csr_with_private_key(abspath(key_path))
            else:
                gen.generate_all()

            print(C.c(C.CYELLOW2, "\nГенерация выполнена!"))
            for ftype, fdata in gen.get_file_list().items():
                if key_path is not None and ftype == 'FILE_KEY':
                    continue
                print("{}: {}".format(ftype, C.c(C.CGREEN2 if fdata['exist'] else C.CRED2, fdata['path'])))
        else:
            print(C.c(C.CRED2, "Вы отменили генерацию!"))


class C:

    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'

    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'

    @staticmethod
    def c(color, text):
        return text
