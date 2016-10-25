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
#         crawler=Crawler('http://www.qiushibaike.com/8hr/page/1',target='/usr/local/qsbk/')
#         crawler=Crawler('http://tieba.baidu.com/p/3138733512',data={'see_lz':1,'pn':1},target='/usr/local/tieba/')
        crawler=Crawler('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8',data={'currentPage':1,'pageSize':100},target='/Users/qupenghui/taomm/')
        crawler.getPage()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()