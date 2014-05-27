#!/usr/bin/env bash

PY3_INS_DIR='/home/toolguy/py34/'
PY3_BIN=$PY3_INS_DIR/bin/python3.4

cd ~
mkdir setup
cd setup
wget https://www.python.org/ftp/python/3.4.0/Python-3.4.0.tgz
tar xzf Python-3.4.0.tgz

cd Python-3.4.0
./configure --prefix=$PY3_INS_DIR
make && make altinstall

wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-3.4.1.tar.gz
tar xzf setuptools-3.4.1.tar.gz
cd setuptools-3.4.1
sudo $PY3_INS_DIR/bin/python3.4 setup.py install

curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | sudo $PY3_INS_DIR/bin/python3.4 -
cd ~
sudo rm -rf setup

$PY3_INS_DIR/bin/pip install PyMySQL
$PY3_INS_DIR/bin/pip install pymongo
$PY3_INS_DIR/bin/pip install pymssql

$PY3_INS_DIR/bin/pip install paramiko
$PY3_INS_DIR/bin/pip install raven
$PY3_INS_DIR/bin/pip install selenium
$PY3_INS_DIR/bin/pip install redis

$PY3_INS_DIR/bin/pip install requests
$PY3_INS_DIR/bin/pip install beautifulsoup4
$PY3_INS_DIR/bin/pip install lxml
$PY3_INS_DIR/bin/pip install simplejson

$PY3_INS_DIR/bin/pip install sphinx
$PY3_INS_DIR/bin/pip install pylint
$PY3_INS_DIR/bin/pip install pep8
$PY3_INS_DIR/bin/pip install openpyxl
$PY3_INS_DIR/bin/pip install XlsxWriter