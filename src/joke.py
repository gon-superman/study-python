#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年10月23日
joke:笑话系列
@author: qupenghui
'''

import re
import os
import threading

class Qsbk(threading.Thread):
    '''
        糗事百科爬虫业务处理
    '''
    def __init__(self,soruce):
        if not os.path.exists(soruce) :
            raise(RuntimeError,'soruce not exists !')
        threading.Thread.__init__(self)
        self.dataList=[]
        self.soruce=soruce
    
    def __loadPage__(self):
        fList = os.listdir(self.soruce)
        for f in fList :
            content = file(self.soruce+f).read()
            self.__parseContent__(content)
        
    def __parseContent__(self,content):
        '''正文内容提取规则：
         id  pattern = article.*?id=\'qiushi_tag_(.*?)\'>
         作者 pattern = re.compile('<div class="author.*?">.*?<h2>(.*?)</h2>.*?',re.S)
         内容 pattern = re.compile('<div class="content">.*?<span>(.*?)</span>',re.S)
         好笑 pattern = re.compile('<span class="stats-vote"><i class="number">(.*?)</i>',re.S)
         评论 pattern = re.compile('<span class="dash">.*?<i class="number">(.*?)</i>',re.S)
        '''
        pattern=re.compile('article.*?id=\'qiushi_tag_(.*?)\'>.*?author.*?<h2>(.*?)</h2>.*?content.*?<span>(.*?)</.*?stats-vote.*?number">(.*?)</.*?dash.*?number">(.*?)</i>',re.S)
        items = re.findall(pattern,content)
        for item in items:
            print item[0],item[1],item[2],item[3],item[4]
#             self.dataList.append([item[0],item[1],item[2],item[3]])
            
    def run(self):
        self.__loadPage__()
        
               

        