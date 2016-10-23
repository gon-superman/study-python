#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os

class Qsbk:
    
    def __init__(self,soruce):
        self.dataList=[]
        self.soruce=soruce
    
    def __loadPage__(self):
        fList = os.listdir(self.soruce)
        for f in fList :
            content = file(self.soruce+f).read()
            self.__parseContent__(content)
        
    def __parseContent__(self,content):
        '''正文内容提取规则：
         作者 pattern = re.compile('<div class="author.*?">.*?<h2>(.*?)</h2>.*?',re.S)
         内容 pattern = re.compile('<div class="content">.*?<span>(.*?)</span>',re.S)
         好笑 pattern = re.compile('<span class="stats-vote"><i class="number">(.*?)</i>',re.S)
         评论 pattern = re.compile('<span class="dash">.*?<i class="number">(.*?)</i>',re.S)
        '''
        pattern=re.compile('<.*?author.*?<h2>(.*?)</h2>.*?content.*?<span>(.*?)</.*?stats-vote.*?number">(.*?)</.*?dash.*?number">(.*?)</i>',re.S)
        items = re.findall(pattern,content)
        for item in items:
            self.dataList.append([item[0],item[1],item[2],item[3]])
            
    def start(self):
        self.__loadPage__()
        print len(self.dataList)
               
qsbk = Qsbk('/usr/local/qsbk/')
qsbk.start()
