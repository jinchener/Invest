#!/usr/bin/env python
#-*-coding: utf-8 -*-
import re
import urllib2
from bs4 import BeautifulSoup as bs
import csv,socket
import os
import time
import random
import cookielib
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

def GetAllLink():
    num=209
    #num = int(raw_input("爬取多少页:>"))
    if not os.path.exists('./data/'):
        os.mkdir('./data/')

    for i in range(74,num):
        url = 'http://www.chinaventure.com.cn/cvsourcemodel/financing/list/0/%s.shtml?keyword=' %(i+1)
        GetPage(url, i)
        '''
        if i+1 == 1:
            url = 'http://www.chinaventure.com.cn/cvsourcemodel/financing/list/0/1.shtml?keyword='
            GetPage(url, i)
        else:
            url = 'http://www.chinaventure.com.cn/cvsourcemodel/financing/list/0/%s.shtml?keyword=' %(i+1)
            GetPage(url, i)
        '''


def GetPage(url, num):
    Url = url
    socket.setdefaulttimeout(30)
    params = {"wd":"a","b":"2"}
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5","Accept": "*/*"}
    cookie = cookielib.MozillaCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    sleepSec = random.randrange(6,10)
    time.sleep(sleepSec)
    req = urllib2.Request(url, headers=i_headers)
    #ser_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'
    #eaders = { 'User-Agent' : user_agent }
    #eq = urllib2.Request(Url, headers = headers)
    page = urllib2.urlopen(req).read().decode('utf-8')
    soup = bs(page, "lxml")
    fixedprice = soup.find_all('tr')      #原价



    atitle = []
    ahref = []
    aprice = []
    afixedprice = []
    adate = []
    csvfile = file('./china-list.csv', 'a')
    writer = csv.writer(csvfile)
    writer.writerow(['融资方','投资机构','融资金额','所属行业','宣布时间','Url'])


    for i in fixedprice:
        ilist=[]
        for j in i.find_all('td'):
            if j.string != None:
                content = j.string
                ilist.append(content)
                #print content
            else:
                content1 = j.find('a')
                str = 'http://www.chinaventure.com.cn'
                content2 = str + content1.get('href')
                ilist.append(content2)
                #print str+content1.get('href') #g.write(u'%s,' % content)
        writer.writerow(ilist)
    print num
    print 'Ok!'
    csvfile.close()


        #g.write('\n')
        #print i.get_text()
        #afixedprice.append(i.get_text())
    #print afixedprice
    #print type(afixedprice)







if __name__ == '__main__':
    GetAllLink()