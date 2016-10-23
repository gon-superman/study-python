#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年10月23日

@author: qupenghui
'''
import unittest
from utils import Crawler

class TestUtils(unittest.TestCase):


    def test_start(self):
        crawler=Crawler('http://www.qiushibaike.com/8hr/page/8','/usr/local/qsbk/')
        crawler.start()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()