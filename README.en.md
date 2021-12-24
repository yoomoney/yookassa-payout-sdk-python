# YooMoney Payout API Python Client Library

[![Build Status](https://travis-ci.org/yoomoney/yookassa-payout-sdk-python.svg?branch=master)](https://travis-ci.org/yoomoney/yookassa-payout-sdk-python)
[![Latest Stable Version](https://img.shields.io/pypi/v/yookassa-payout.svg)](https://pypi.org/project/yookassa-payout/)
[![Total Downloads](https://img.shields.io/pypi/dm/yookassa-payout.svg)](https://pypi.org/project/yookassa-payout/)
[![License](https://img.shields.io/pypi/l/yookassa-payout.svg)](https://github.com/yoomoney/yookassa-payout-sdk-python)

[Russian](https://github.com/yoomoney/yookassa-payout-sdk-python/blob/master/README.md) | English

Client to work on the [Protocol for mass payouts](https://yookassa.ru/docs/payouts/api/using-api/basics?lang=en)

## Opportunities
You can with this SDK:
1. [Generate a certificate](https://yookassa.ru/docs/payment-solution/supplementary/security?lang=en) for interaction with YooMoney.
2. [Transfer money](https://yookassa.ru/docs/payouts/api/make-deposition/basics?lang=en) to individuals for wallets in YooMoney, mobile phone numbers, Bank cards and accounts (makeDeposition).
3. [To test the possibility of transfer of remittances](https://yookassa.ru/docs/payouts/api/make-deposition/basics?lang=en#test-deposition) to wallets in YooMoney (testDeposition).
4. [Keep track of the balance of payouts](https://yookassa.ru/docs/payouts/api/balance?lang=en) (balance).
5. [Receive notifications](https://yookassa.ru/docs/payouts/api/error-deposition-notification?lang=en) the unsuccessful status of transfers to a Bank account, card, or mobile phone (errorDepositionNotification).

## Requirements
* Python 3.5 (or later version)
* pip

## Installation
### Under console using pip

1. Install pip.
2. In the console, run the following command:
```bash
pip install yookassa-payout
```

### Under console using easy_install
1. Install easy_install.
2. In the console, run the following command:
```bash
easy_install --upgrade yookassa-payout
```

### Manually
1. In the console, run the following command:
```bash
wget https://github.com/yoomoney/yookassa-payout-sdk-python/archive/master.zip
tar zxf yookassa-payout-sdk-python-master.tar.gz
cd yookassa-payout-sdk-python-master
python setup.py install
```

## Getting a certificate for authenticating requests
To interact with YooMoney.The cashier must obtain a certificate. For this:
1. Create a private key and a certificate request (CSR).
2. Fill out the certificate application form.
3. Exchange data with YooMoney.

### Step 1. Creating a private key and CSR

#### Using the SDK method
1. Import classes to create CSR
```python
from yookassa_payout.domain.models.organization import Organization
from yookassa_payout.payout import Payout
```

2. Create an instance of the `Organization` class with data for creating the request. All data must be entered in Latin.
```python
org = Organization({
    "org_name": "YooMoney",              # Organization Name (Latin)
    "common_name": "/business/yoomoney", # Common Name, for example the name of your organization; must start with «/business/»
    "email": "cms@yoomoney.ru"           # Email
})
```
3. Create a CSR and a private key.
```python
# Specify the location where the files should be saved and the password for the private key (if necessary)
Payout.get_csr(org, './files/output', '12345')
```
As a result, the SDK will generate a private key, CSR, and a text file with an electronic signature (necessary for further steps).

#### Via the console
1. In the console, go to your project folder.
```bash
cd '<your project folder>'
```

2. Execute the command:
```
yookassa-payout -getcsr
```

3. Enter data for the certificate, following the instructions on the screen. The text must be entered in Latin letters.
As a result, the SDK will generate a private key, CSR, and a text file with an electronic signature (necessary for further steps).

### Step 2. Filling out the certificate application
[Download the application](https://yookassa.ru/docs/ssl_cert_form.doc) to the certificate, fill it out and print it out. Sign and seal the document. Scan.

| **Parameter**                                    | **Description**                                                                                                                                                                                                                                                                                                                                                             |
|:-------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CN                                               | Must match the value of the Common Name parameter (eg, YOUR name). For example, */business/predpriyatie*.                                                                                                                                                                                                                                                                   |
| Electronic signature of the certificate request  | The text view obtained in the previous step.                                                                                                                                                                                                                                                                                                                                |
| Organization name in Latin letters               | Must match the value of the Organization Name parameter (eg, company) *Internet Widgits Pty Ltd*.                                                                                                                                                                                                                                                                           |
| The reason for the request                       | Possible options: <ul><li>*initial* — to get the first certificate;</li><li>*scheduled replacement* — to replace a certificate that has expired;</li><li>*replacement of a compromised* — to replace a previously issued certificate in the event of a security breach;</li><li>*adding a server* — to use the new certificate on additional servers or services.</li></ul> |
| Contact person (full name, phone number, e-mail) | Contact a specialist to contact you if you have any questions about the issued certificate.                                                                                                                                                                                                                                                                                 |

### Step 3. Data exchange with YooMoney
Send the certificate request file (request.csr) and a scan of the request by email to your YooMoney Manager.Box office.
In response to the request, the Manager will send a file with the certificate within 2 business days. The certificate is valid for 1 year.
Place the received certificate on your server

## Start of work
1. Determine what types of payouts you need and whether you want to check your balance.
2. Import required classes
```python
from yookassa_payout.domain.common.keychain import KeyChain
from yookassa_payout.configuration import Configuration
from yookassa_payout.payout import Payout
```

3. Import the classes you need to solve your problems.
4. Create an instance of the `KeyChain` class by passing the path to the public key, the path to the private key, and, if necessary, the password for the private key.
```python
keychain = KeyChain('publicCert.cer', 'privateCert.pem', 'password')
```

5. Create an instance of the `Client` class and pass the gateway ID from the [merchant profile](https://yookassa.ru/my) YooMoney and instance of the `KeyChain` class.
```python
Configuration.configure('000000', keychain)
```

6. Call the appropriate method. [More information about making payouts](https://yookassa.ru/docs/payouts/api/using-api/basics?lang=en)

#### Example of payout to a Bank account
```python
# Importing classes
from yookassa_payout.configuration import Configuration
from yookassa_payout.payout import Payout
from yookassa_payout.domain.common.keychain import KeyChain
from yookassa_payout.domain.models.recipients.bank_account_recipient import BankAccountRecipient
from yookassa_payout.domain.request.make_deposition_request import MakeDepositionRequest

# Creating a housekeeper and saving settings
keychain = KeyChain('./files/250000.cer', './files/privateKey.pem', '12345')
Configuration.configure(250000, keychain)

# Getting the current balance
balance = Payout.get_balance()

# The compilation of data on the beneficiary
recipient = BankAccountRecipient()
recipient.pof_offer_accepted = True
recipient.bank_name = 'Barclays'
recipient.bank_city = 'London'
recipient.bank_cor_account = '30101810400000000225'
recipient.customer_account = '40817810255030943620'
recipient.bank_bik = '042809679'
recipient.payment_purpose = 'Refund under the agreement 25-001, without VAT'
recipient.pdr_first_name = 'John'
recipient.pdr_last_name = 'Watson'
recipient.pdr_doc_number = '4002109067'
recipient.pdr_doc_issue_date = '1999-07-30'
recipient.pdr_address = 'Baker street, 221'
recipient.pdr_birth_date = '1987-05-24'
recipient.sms_phone_number = '79653457676'

# Preparing a request to create a payout
request = MakeDepositionRequest()
request.agent_id = 250000
request.client_order_id = '215d8da0-000f-50be-b000-0003308c89be'
request.request_dt = '2020-03-04T15:39:45.456+03:00'
request.payment_params = recipient

# The carrying out of the payout
result = Payout.create_deposition(request)
```
