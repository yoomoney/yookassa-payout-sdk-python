# -*- coding: utf-8 -*-
import argparse
import sys

import yookassa_payout
from yookassa_payout.domain.common.cli_client import CliClient


def main():

    parser = argparse.ArgumentParser(
        add_help=False,
        description='Консольный скрипт пакета yookassa_payout.',
        epilog='Author: {}\nE-mail: {}\nVersion: {}'.format(yookassa_payout.__author__,
                                                            yookassa_payout.__email__,
                                                            yookassa_payout.__version__)
    )

    parser.version = yookassa_payout.__version__
    parser.add_argument('-getcsr', action='store_const', const=True, help='Генерация сертификата и ключей')
    parser.add_argument('-k', dest="key", help='Для генерации сертификата с собственным ключом')
    parser.add_argument('-v', '--version', action='version', help='Показать версию программы и выйти')
    parser.add_argument('-h', '--help', action='help', help='Показать текст справки и выйти')
    args = parser.parse_args()

    if args.getcsr is not None:
        cli = CliClient()
        cli.generate(args.key)
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
