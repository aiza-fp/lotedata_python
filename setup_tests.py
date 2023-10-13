# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

from __future__ import print_function

import os
import subprocess

from setuptools import setup, find_packages


data_files = []

if os.path.exists("tests"):
    data_files.append(('/data/tests/lotedata', ['tests/test_tp_lotedata.py']))
    data_files.append(('/data/tests/lotedata', [
        '../../tests/sawtooth_integration/tests/test_lotedata_smoke.py']))

try:
    os.environ["ST_VERSION"]
    print('Using ST_VERSION')
    VERSION = os.environ["ST_VERSION"]
except KeyError:
    print('ST_VERSION not set. Using get_version')
    VERSION = subprocess.check_output(
        ['../../bin/get_version']).decode('utf-8').strip()

setup(
    name='sawtooth-lotedata-tests',
    version=VERSION,
    description='Sawtooth Lotedata Python Test',
    author='Hyperledger Sawtooth',
    url='https://github.com/hyperledger/sawtooth-sdk-python',
    packages=find_packages(),
    install_requires=[
        "cbor",
        "colorlog",
        "sawtooth-sdk",
    ],
    data_files=data_files,
    entry_points={
        'console_scripts': [
            'lotedata = sawtooth_lotedata.client_cli.lotedata_cli:main_wrapper',
            'lotedata-tp-python = sawtooth_lotedata.processor.main:main'
        ]
    })
