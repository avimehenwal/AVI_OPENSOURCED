#!/usr/bin/env bash

PY3_INS_DIR='/home/toolguy/py34/'
PY3_BIN=$PY3_INS_DIR/bin/python3.4

cd ~
mkdir setup
cd setup
wget --no-check-certificate https://www.python.org/ftp/python/3.4.0/Python-3.4.0.tgz
tar xzf Python-3.4.0.tgz

cd Python-3.4.0
./configure --prefix=$PY3_INS_DIR
make && make altinstall

sudo $PY3_INS_DIR/bin/python3.4/easy_install pip
