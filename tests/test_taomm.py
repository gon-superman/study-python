#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年10月23日

@author: qupenghui
'''
import unittest
from taomm import Taomm


class TestTaomm(unittest.TestCase):


    def test_start(self):
        taomm = Taomm('/Users/qupenghui/taomm/')
        taomm.start()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()