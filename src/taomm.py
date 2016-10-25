#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年10月24日
@author: qupenghui

使用到demjson包，需单独安装：
1、下载demjson http://deron.meranda.us/python/demjson/download
2、解压安装
tar -xvzf demjson-2.2.3.tar.gz
cd demjson-2.2.3

python setup.py install
Mac下intall权限问题：sudo python ./setup.py install
'''
import demjson
import threading
import os
from utils import Crawler

class Taomm(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self, source):
        '''
        Constructor
        '''
        if not os.path.exists(source) :
            raise(RuntimeError,'soruce not exists !')
        threading.Thread.__init__(self)
        self.source=source
        
    def __parseJson__(self):
        fList = os.listdir(self.source)
        for f in fList :
            print f
            content = file(self.source+f).read()
            json=demjson.decode(content,'gbk')
            self.__parseDOList__(json['data']['searchDOList'])
            
    def __parseDOList__(self,items):
        for item in items :
            crawler = Crawler('http:'+item['avatarUrl'],target=self.source)
            crawler.getImage()
            print item['realName'],item['city'],item['height'],item['avatarUrl']
        
            
    def run(self):
        self.__parseJson__()