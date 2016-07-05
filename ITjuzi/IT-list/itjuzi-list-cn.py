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
import string
import types


def GetAllLink():
    num=1213
    #num = int(raw_input("爬取多少页:>"))
    if not os.path.exists('./data/'):
        os.mkdir('./data/')

    for i in range(182,num):

        '''
        url = 'https://www.itjuzi.com/investevents?page=%s' %(i+1)
        GetPage(url, i)
        '''
        if i+1 == 1:
            url = 'https://www.itjuzi.com/investevents/'
            GetPage(url, i)
        else:
            url = 'https://www.itjuzi.com/investevents?page=%s' %(i+1)
            GetPage(url, i)
        



def GetPage(url, num):
    #Url = url
    socket.setdefaulttimeout(30)
    params = {"wd":"a","b":"2"}
    enable_proxy = True
    proxy = urllib2.ProxyHandler({"http" : "http://121.31.145.149:8123"})
    proxy_support = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

    Url='https://www.itjuzi.com/investevents?page=%s' %(num)
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5","Accept": "*/*",'Referer':Url}
    cookie = cookielib.MozillaCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url, headers=i_headers)
    sleepSec = random.randrange(6,10)
    time.sleep(sleepSec)
    #ser_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'
    #eaders = { 'User-Agent' : user_agent }
    #eq = urllib2.Request(Url, headers = headers)
    page = urllib2.urlopen(req).read().decode('utf-8')
    #print page
    soup = bs(page, "lxml")
    page=soup.find_all("ul","list-main-eventset")[1]
    detail = page.find_all('li')      #原价
    #print detail


    #csvfile = file('./ticket.csv', 'w')
    #csvfile.write('\xEF\xBB\xBF');
    #writer = csv.writer(csvfile,quotechar='|')
    #writer.writerow(['时间','Url','公司','所属行业','地区','轮次','融资额','投资方'])
    f = open("itjuzi-list-cn.txt",'a')
    f.write("Url|时间|公司|所属行业|地区|轮次|融资额|投资方")
    f.write("\n")

    for i in detail:
        if i.find("span", "investorset").find("span") != None:
            date = i.find("i", "cell round").get_text().encode("utf-8").replace("\n", " ").replace("\t", " ").replace("\r", " ").replace(" ", "")  # .contents[1].contents
            Url = i.find("i", "cell pic").find('a').get('href')
            deal = i.contents[8]
            company = i.contents[6].get_text().encode("utf-8").replace("\n", " ").replace("\t", " ").replace("\r"," ").replace(" ", "")
            area = deal.find("span", "tags t-small c-gray-aset").get_text().encode("utf-8").replace("\n", " ").replace("\t", " ").replace("\r", " ").replace(" ", "")  # .contents[1].contents
            location = deal.find("span", "loca c-gray-aset t-small").get_text().encode("utf-8").replace("\n"," ").replace("\t", " ").replace("\r", " ").replace(" ", "")  # .contents[1].contents
            around = i.find_all("i", "cell round")[1].get_text().encode("utf-8").replace("\n", " ").replace("\t"," ").replace("\r", " ").replace(" ", "")  # .contents[1].contents[0].contents
            number = i.find("i", "cell fina").get_text().encode("utf-8").replace("\n", " ").replace("\t", " ").replace( "\r", " ").replace(" ", "")
            investorset = i.find("span", "investorset").get_text().encode("utf-8")
            investor1 = investorset.replace("\n", " ").lstrip().rstrip().replace(" ", ",")
            message = Url + '|' + date + '|' + company + '|' + area + '|' + location + '|' + around + '|' + number + '|' + investor1
            end = message.encode("utf-8").replace('\n', '').replace('\t', '').replace(" ", "")
            f.write(end)
            f.write('\n')




        #company = deal.find(target="_blank" )
        #print company
        '''
        area = deal.find("span","tags t-small c-gray-aset").string
        location = deal.find("span","loca c-gray-aset t-small").string
        around = i.find_all("i","cell round")[1].string
        number = i.find("i","cell fina").string
        investor = i.find("i","cell date").string
        message = time +'|'+Url+'|'+company+ '|'+ area +'|'+ location +'|'+ around  +'|'+ number +'|'+ investor
        writer.writerow([str(message).split('|')])
        '''
    print num
    print  'Ok!'
    #csvfile.close()
    f.close()


'''

        ilist=[]
        for j in i.find_all('td'):
            if j.string != None:
                content = j.string
                ilist.append(content)
                print content
            else:
                content1 = j.find('a')
                str = 'http://www.chinaventure.com.cn'
                content2 = str + content1.get('href')
                ilist.append(content2)
                print str+content1.get('href') #g.write(u'%s,' % content)
        writer.writerow(ilist)
'''




        #g.write('\n')
        #print i.get_text()
        #afixedprice.append(i.get_text())
    #print afixedprice
    #print type(afixedprice)







if __name__ == '__main__':
    GetAllLink()