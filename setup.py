#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from setuptools import setup, find_packages  # type: ignore

with open("README.en.md") as readme_file:
    readme = readme_file.read()

with open('src/yookassa_payout/__init__.py', encoding='utf8') as fp:
    version = re.search(r"__version__\s*=\s*'(.*)'", fp.read()).group(1)

setup(
    name="yookassa-payout",
    author="YooMoney",
    author_email="cms@yoomoney.ru",
    version=version,
    python_requires=">=3.5",
    keywords="yoomoney, yookassa, payout, sdk, python",
    description="YooKassa Payout API SDK Python Library",
    entry_points={"console_scripts": ["yookassa-payout=yookassa_payout.cli:main", ], },
    install_requires=['urllib3', 'requests', 'lxml', 'python-dateutil', 'pyOpenSSL'],
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"yookassa_payout": ["py.typed"]},
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages('src'),
    setup_requires=[],
    url="https://github.com/yoomoney/yookassa-payout-sdk-python",
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Russian",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
