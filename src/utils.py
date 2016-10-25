#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2016年10月23日
@author: qupenghui
'''
import urllib
import urllib2
import os
import time

class Crawler():
    '''
    爬虫，负责爬取网页并存储在相应目录
    '''
    def __init__(self,url,data=None,target=None):
        if not os.path.exists(target) :
            os.mkdir(target)
            print 'target not exits,mkdir:%s' %target
        
#         threading.Thread.__init__(self)
        
        self.headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        #     'Accept-Encoding':'gzip, deflate, sdch',
            'Connection':'keep-alive',
            'Cache-Control':'max-age=0',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        self.url=url
        self.data=data
        self.target=target
        
    def __getContent__(self):
        try:
            data = None
            if self.data is not None :
                data=urllib.urlencode(self.data)
            request=urllib2.Request(self.url,data=data,headers=self.headers)
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
        name=self.target+time.strftime('%Y%m%d%H%M%S')+'.html'
        f=file(name,'w')
        f.write(content)
        f.close()
        print 'save a page:%s' %(name)
    
    def __saveImage__(self,content): 
        name=self.target+time.strftime('%Y%m%d%H%M%S')+'.jpg'
        f=file(name,'wb')
        f.write(content)
        f.close()
        print 'save a image:%s' % name       
            
    def getPage(self):
        content = self.__getContent__();    
        self.__savePage__(content)
        
    def getImage(self):
        content = self.__getContent__();    
        self.__saveImage__(content)
        
