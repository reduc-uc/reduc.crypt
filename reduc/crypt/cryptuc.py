#! /usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2010. Jose Dinuncio
# All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License.
#
##############################################################################
import crypt
import base64
import random
import string
import hashlib

class Crypt:
    @staticmethod
    def encode(pwd='', salt='', method='crypt', encode=True):
        if not encode:
            return pwd

        if method == 'crypt':
            return Crypt.crypt(pwd, salt)
        else :
            return Crypt.sha(pwd, salt)

    @staticmethod
    def crypt(pwd='', salt=''):
        pwd = pwd or Crypt._randomString(8)
        salt = salt or Crypt._randomString(8)
        salt = '$1${0}$'.format(salt)
        return '{crypt}%s' % crypt.crypt(pwd, salt)

    @staticmethod
    def sha(pwd='', salt=''):
        pwd = pwd or Crypt._randomString(8)
        salt = salt or Crypt._randomString(8)
        s = hashlib.sha1()
        s.update(pwd)
        s.update(salt)
        encoded = base64.encodestring(s.digest()+salt).rstrip()
        return '{SSHA}%s' % encoded

    @staticmethod
    def _randomString(l=8):
        return ''.join([random.choice(string.ascii_letters) for i in range(l)])



