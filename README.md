# YooKassa Payout API Python Client Library

[![Build Status](https://travis-ci.org/yoomoney/yookassa-payout-sdk-python.svg?branch=master)](https://travis-ci.org/yoomoney/yookassa-payout-sdk-python)
[![Latest Stable Version](https://img.shields.io/pypi/v/yookassa-payout.svg)](https://pypi.org/project/yookassa-payout/)
[![Total Downloads](https://img.shields.io/pypi/dm/yookassa-payout.svg)](https://pypi.org/project/yookassa-payout/)
[![License](https://img.shields.io/pypi/l/yookassa-payout.svg)](https://github.com/yoomoney/yookassa-payout-sdk-python)

Russian | [English](https://github.com/yoomoney/yookassa-payout-sdk-python/blob/master/README.en.md)

Клиент для работы по [Протоколу массовых выплат](https://yookassa.ru/docs/payouts/api/using-api/basics)

## Возможности
С помощью этого SDK вы можете:
1. [Генерировать сертификат](https://yookassa.ru/docs/payment-solution/supplementary/security) для взаимодействия с ЮKassa.
2. [Переводить деньги](https://yookassa.ru/docs/payouts/api/make-deposition/basics) физическим лицам на кошельки в ЮMoney, номера мобильных телефонов, банковские карты и счета (makeDeposition).
3. [Проверять возможность](https://yookassa.ru/docs/payouts/api/make-deposition/basics#test-deposition) зачисления переводов на кошельки в ЮMoney (testDeposition).
4. [Отслеживать баланс выплат](https://yookassa.ru/docs/payouts/api/balance) (balance).
5. [Получать уведомления](https://yookassa.ru/docs/payouts/api/error-deposition-notification) о неуспешном статусе переводов на банковский счет, карту, мобильный телефон (errorDepositionNotification).

## Требования
* Python 3.5 (и выше)
* pip

## Установка
### С помощью pip

1. Установите pip.
2. В консоли выполните команду
```bash
pip install yookassa-payout
```

### С помощью easy_install
1. Установите easy_install.
2. В консоли выполните команду
```bash
easy_install --upgrade yookassa-payout
```

### Вручную

1. В консоли выполните команды:
```bash
wget https://github.com/yoomoney/yookassa-payout-sdk-python/archive/master.zip
tar zxf yookassa-payout-sdk-python-master.tar.gz
cd yookassa-payout-sdk-python-master
python setup.py install
```


### С помощью easy_install
1. Установите easy_install.
2. В консоли выполните команду
```bash
easy_install --upgrade yookassa_payout
```

### Вручную

1. В консоли выполните команды:
```bash
wget https://github.com/yoomoney/yookassa-payout-sdk-python/archive/master.zip
tar zxf yookassa-payout-sdk-python-master.tar.gz
cd yookassa-payout-sdk-python-master
python setup.py install
```


## Получение сертификата для аутентификации запросов
Для взаимодействия с ЮKassa необходимо получить сертификат. Для этого:
1. Создайте приватный ключ и запрос на получение сертификата (CSR).
2. Заполните заявку на сертификат.
3. Обменяйтесь данными с ЮKassa.

### Шаг 1. Создание приватного ключа и CSR

#### С помощью метода SDK
1. Импортируйте классы для создания CSR
```python
from yookassa_payout.domain.models.organization import Organization
from yookassa_payout.payout import Payout
```

2. Создайте экземпляр класса `Organization` с данными для создания заявки. Все данные нужно вводить латиницей.
```python
org = Organization({
    "org_name": "YooMoney",              # Название вашей организации (латиницей)
    "common_name": "/business/yoomoney", # Имя сервера без пробелов, например название вашей организации; должно начинаться с «/business/»
    "email": "cms@yoomoney.ru"           # Адрес электронной почты
})
```

3. Создайте CSR и приватный ключ.
```python
# Укажите место, куда должны сохраниться файлы, и пароль для приватного ключа (при необходимости)
Payout.get_csr(org, './files/output', '12345')
```

В результате SDK сгенерирует приватный ключ, CSR и текстовый файл с электронной подписью (нужно для дальнейших шагов).

#### Через консоль
1. В консоли перейдите в папку вашего проекта.
```bash
cd '<путь к проекту>'
```

2. Выполните команду:
```
yookassa-payout -getcsr
```

3. Введите данные для сертификата, следуя указаниям на экране. Текст необходимо вводить латинскими буквами.
В результате SDK сгенерирует приватный ключ, CSR и текстовый файл с электронной подписью (нужно для дальнейших шагов).

### Шаг 2. Заполнение заявки на сертификат
[Скачайте заявку](https://yookassa.ru/docs/ssl_cert_form.doc) на сертификат, заполните и распечатайте. Поставьте подпись и печать. Отсканируйте.

| **Параметр**                                | **Описание**                                                                                                                                                                                                                                                                                                                                                                                           |
|:--------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CN                                          | Должно соответствовать значению параметра Common Name (eg, YOUR name). Например, /business/predpriyatie.                                                                                                                                                                                                                                                                                               |
| Электронная подпись запроса на сертификат   | Текстовое представление, полученное на предыдущем шаге.                                                                                                                                                                                                                                                                                                                                                |
| Наименование организации латинскими буквами | Должно соответствовать значению параметра Organization Name (eg, company) *Internet Widgits Pty Ltd*.                                                                                                                                                                                                                                                                                                  |
| <span align="top">Причина запроса</span>    | Возможные варианты: <ul><li>первоначальный — для получения первого сертификата;</li><li>плановая замена — для замены сертификата, у которого закончился срок действия;</li><li>замена скомпрометированного — для замены ранее выпущенного сертификата при нарушении безопасности;</li><li>добавление сервера — для использования нового сертификата на дополнительных серверах или сервисах.</li></ul> |
| Контактное лицо (ФИО, телефон, e-mail)      | Контакты специалиста для связи при возникновении вопросов по выданному сертификату.                                                                                                                                                                                                                                                                                                                    |

### Шаг 3. Обмен данными с ЮKassa
Отправьте файл запроса на сертификат (request.csr) и скан заявки по электронной почте своему менеджеру ЮKassa. В ответ на заявку менеджер в течение 2 рабочих дней пришлет файл с сертификатом. Срок действия сертификата 1 год.
Разместите полученный сертификат на своем сервере

## Начало работы
1. Определите, какие виды выплат вам нужны и хотите ли вы проверять баланс.
2. Импортируйте обязательные классы
```python
from yookassa_payout.domain.common.keychain import KeyChain
from yookassa_payout.configuration import Configuration
from yookassa_payout.payout import Payout
```

3. Импортируйте классы, необходимые для решения ваших задач.
4. Создайте экземпляр класса `KeyChain`, передав в него путь к публичному ключу, путь к приватному ключу и, при необходимости, пароль приватного ключа.
```python
keychain = KeyChain('publicCert.cer', 'privateCert.pem', 'password')
```

5. Создайте экземпляр класса `Client` и передайте идентификатор шлюза из [личного кабинета](https://yookassa.ru/my) ЮKassa и экземпляр класса `KeyChain`.
```python
Configuration.configure('000000', keychain)
```

6. Вызовите нужный метод. [Подробнее о проведении выплат](https://yookassa.ru/docs/payouts/api/using-api/basics)

#### Пример выплаты на банковский счет
```python
# Импорт классов
from yookassa_payout.configuration import Configuration
from yookassa_payout.payout import Payout
from yookassa_payout.domain.common.keychain import KeyChain
from yookassa_payout.domain.models.recipients.bank_account_recipient import BankAccountRecipient
from yookassa_payout.domain.request.make_deposition_request import MakeDepositionRequest

# Создание ключницы и сохранение настроек
keychain = KeyChain('./files/250000.cer', './files/privateKey.pem', '12345')
Configuration.configure(250000, keychain)

# Получение текущего баланса
balance = Payout.get_balance()

# Подготовка данных о получателе выплаты
recipient = BankAccountRecipient()
recipient.pof_offer_accepted = True
recipient.bank_name = 'ПАО Сбербанк'
recipient.bank_city = 'г.Москва'
recipient.bank_cor_account = '30101810400000000225'
recipient.customer_account = '40817810255030943620'
recipient.bank_bik = '042809679'
recipient.payment_purpose = 'Возврат по договору 25-001, без НДС'
recipient.pdr_first_name = 'Владимир'
recipient.pdr_middle_name = 'Владимирович'
recipient.pdr_last_name = 'Владимиров'
recipient.pdr_doc_number = '4002109067'
recipient.pdr_doc_issue_date = '1999-07-30'
recipient.pdr_address = 'пос.Большие Васюки, ул.Комиссара Козявкина, д.4'
recipient.pdr_birth_date = '1987-05-24'
recipient.sms_phone_number = '79653457676'

# Подготовка запроса на создание выплаты
request = MakeDepositionRequest()
request.agent_id = 250000
request.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
request.request_dt = '2020-03-04T15:39:45.456+03:00'
request.payment_params = recipient

# Проведение выплаты
result = Payout.create_deposition(request)
```
