# -*- coding: utf-8 -*-

import re
from setuptools import setup
 
 
version = re.search('^__version__\s*=\s*"(.*)"',
                    open('emailsender/__init__.py').read(), re.M).group(1)
 
 
with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="emailsender",
    packages=["emailsender"],
    entry_points={
        "console_scripts": ['emailsender = emailsender.mail:main']
    },
    version=version,
    description="Cli-tool for sending emails throw specified SMTP server.",
    long_description=long_descr,
    author="Yuri Shikanov",
    author_email="dizballanze@gmail.com",
    url="https://github.com/dizballanze/mailsender",
    license="MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
