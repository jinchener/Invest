#!/usr/bin/env python
#-*-coding: utf-8 -*-
import re
import urllib2
from bs4 import BeautifulSoup as bs
import csv
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def GetAllLink():
    num = int(raw_input("爬取多少页:>"))
    if not os.path.exists('./data/'):
        os.mkdir('./data/')

    for i in range(num):
        if i+1 == 1:
            url = 'http://nj.58.com/piao/'
            GetPage(url, i)
        else:
            url = 'http://nj.58.com/piao/pn%s/' %(i+1)
            GetPage(url, i)


def GetPage(url, num):
    Url = url
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(Url, headers = headers)
    page = urllib2.urlopen(req).read().decode('utf-8')
    soup = bs(page)
    table = soup.table
    tag = table.find_all('tr')
    # 提取出所需的那段
    soup2 = bs(str(tag))
    title = soup2.find_all('a','t')         #标题与url
    price = soup2.find_all('b', 'pri')      #价格
    fixedprice = soup2.find_all('del')      #原价
    date = soup2.find_all('span','pr25')    #时间

    atitle = []
    ahref = []
    aprice = []
    afixedprice = []
    adate = []

    for i in title:
        #print i.get_text(), i.get('href')
        atitle.append(i.get_text())
        ahref.append(i.get('href'))
    for i in price:
        #print i.get_text()
        aprice.append(i.get_text())
    for i in fixedprice:
        #print j.get_text()
        afixedprice.append(i.get_text())
    for i in date:
        #print i.get_text()
        adate.append(i.get_text())

    csvfile = file('./data/ticket_%s.csv'%num, 'w')
    writer = csv.writer(csvfile)
    writer.writerow(['标题','url','售价','原价','演出时间'])
    '''
    每个字段必有title，但是不一定有时间date
    如果没有date日期，我们就设为'---'
    '''
    if len(atitle) > len(adate):
        for i in range(len(atitle) - len(adate)):
            adate.append('---')

    for i in range(len(atitle)):
            message = atitle[i]+'|'+ahref[i]+'|'+aprice[i]+ '|'+afixedprice[i]+'|'+ adate[i]
            writer.writerow([i for i in str(message).split('|')])
    print "[Result]:> 页面 %s 信息保存完毕!"%(num+1)
    csvfile.close()






if __name__ == '__main__':
    GetAllLink()