#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
selenium安装：
1、下载selenium安装包
https://pypi.python.org/pypi/selenium#downloads
2、解压并安装
sudo python ./setup.py install

Created on 2016年10月26日
@author: qupenghui
'''
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.maximize_window()
q=browser.find_element_by_id('kw')
q.send_keys('python')
browser.find_element_by_id('su').click()
time.sleep(3)
browser.quit()