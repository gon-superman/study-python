#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年10月23日

@author: qupenghui
'''
import unittest
from joke import Qsbk


class TestQsbk(unittest.TestCase):


    def test_start(self):
        qsbk = Qsbk('/usr/local/qsbk/')
        qsbk.start()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()