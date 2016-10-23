#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
import os
import time

class Crawler:
    '''
    爬虫，负责爬取网页并存储在相应目录
    '''
    def __init__(self,url,target):
        self.headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        #     'Accept-Encoding':'gzip, deflate, sdch',
            'Connection':'keep-alive',
            'Cache-Control':'max-age=0',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        self.url=url
        self.target=target
        
    def __getPage__(self):
        try:
            request=urllib2.Request(self.url,headers=self.headers)
            response = urllib2.urlopen(request)
            content=response.read()
            return content
        except urllib2.URLError,e :
            if hasattr(e, 'code'):
                print e.code
            if hasattr(e, 'reason'):
                print e.reason
            return None
        
    def __savePage__(self,content):
        if os.path.exists(self.target) :
            name=self.target+time.strftime('%Y%m%d%H%M%S')+'.txt'
            f=file(name,'w')
            f.write(content)
            f.close()
            print 'save a page:%s' %(name)
        else :
            print 'target not exists !'
            
    def start(self):
        content = self.__getPage__();
        self.__savePage__(content)

crawler=Crawler('http://www.qiushibaike.com/8hr/page/4','/usr/local/qsbk/')
crawler.start()