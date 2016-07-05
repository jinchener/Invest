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



    file_object_Z = open("itjuzi-result.txt", "wb")
    file = open("list1.txt")
    num=0


    try:
        line = file.readlines()
        for i in line:
            line1=i.replace('\n','' ).rstrip()
            print line1
            print len(line1)
            file_object_Z.write("Url|标题|时间|介绍|公司|所属行业|子行业|地区|轮次|融资额|股权占比|投资方")
            file_object_Z.write("\n")
            num=num+1
            GetPage(line1,num,file_object_Z)   
                
         
            
            #mySpider.downAndWriteOneUrl(line,line,file_object_Z,True)



    finally:
        file_object_Z.close()
        file.close()



def GetPage(url, num,file_object_Z):
    #Url = url
    socket.setdefaulttimeout(30)
    params = {"wd":"a","b":"2"}
    enable_proxy = True
    proxy = urllib2.ProxyHandler({"http" : "http://121.31.145.149:8123"})
    proxy_support = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

    #Url='https://www.itjuzi.com/investevents?page=%s' %(num)
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5","Accept": "*/*"}
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
    #print soup
    page1=soup.find_all("div","sec")[2]
    #print page1.find("div","titlebar-center").next_siblings
    head=page1.find("div","titlebar-center").find_all("p")    
    ilist=[]
    for i in head:
        title=i.get_text()
        ilist.append(title)    
    head1 = page1.find("div", "titlebar-center").next_siblings
    for i in head1:
        if i.find("p")!=None:
            if i.find("p")!=-1:
                dis=i.get_text()
    ilist.append(dis)
    body=page1.find("div","block-inc-fina")
    bodylist= body.find_all("td")
    company=bodylist[1].find("a").get_text()
    area1=bodylist[1].find_all("a")[1].get_text()
    area2=bodylist[1].find_all("span")[0].get_text()
    locate=bodylist[1].find_all("span")[1].get_text()
    ilist.append(company)
    ilist.append(area1)
    ilist.append(area2)
    ilist.append(locate)
    round=body.find("td","tac").find_all("span")[1].get_text()
    ilist.append(round)
    fina=body.find_all("td","tac")[1].find_all("span")[1].get_text()
    ilist.append(fina)
    percent=body.find_all("td","tac")[2].find_all("span")[1].get_text()    
    ilist.append(percent)
    head2 = page1.find_all("div", "titlebar-center")[1].next_siblings
    investlist=[]
    for i in head2:
        if i.find("h4")!= -1:
            for j in i.find_all("h4"):
                investor1=j.find("a").get_text()
                investlist.append(investor1)    
    investor=','.join(investlist)
    ilist.append(investor)
    message=url+'|'+'|'.join(ilist).replace("\n","").replace(" ","").replace("\t","")
    file_object_Z.write(message)
    file_object_Z.write("\n")
    print num
    print 'Ok!'



    #print ilist

    #print type(page1.get_text())
    #detail = page.find_all('li')      #原价
    #print detail

'''
    #csvfile = file('./ticket.csv', 'w')
    #csvfile.write('\xEF\xBB\xBF');
    #writer = csv.writer(csvfile,quotechar='|')
    #writer.writerow(['时间','Url','公司','所属行业','地区','轮次','融资额','投资方'])
    f = open("itjuzi-list-foreign.txt",'a')
    f.write("Url|时间|公司|所属行业|地区|轮次|融资额|投资方")
    f.write("\n")



    for i in detail:
        date= i.find("i","cell round").get_text().encode("utf-8") #.contents[1].contents
        Url = i.find("i","cell pic").find('a').get('href')
        deal=i.contents[8]
        company =  i.contents[6].get_text().encode("utf-8")
        area =  deal.find("span","tags t-small c-gray-aset").get_text().encode("utf-8")#.contents[1].contents
        location = deal.find("span","loca c-gray-aset").get_text().encode("utf-8")#.contents[1].contents
        around = i.find_all("i","cell round")[1].get_text().encode("utf-8")#.contents[1].contents[0].contents
        number = i.find("i","cell fina").string.replace('\n', '')
        if len(i.find("i","cell date").find_all("a")) >1:
            investor = i.find("i","cell date").find_all("a")
            ilist=[]
            for j in investor:
                invest = j.get_text()
                ilist.append(invest)
                investor1 =','.join(ilist)
        else:
            investor1 = i.find("i","cell date").get_text()
        #print investor1



        message = Url+'|'+date +'|'+company+ '|'+ area +'|'+ location +'|'+ around  +'|'+ number +'|'+ investor1
        end = message.encode("utf-8").replace('\n', '').replace('\t', '')
        f.write(end)
        f.write('\n')
        #writer.writerow([str(end).split('|')])
        #print investor

        #company = deal.find(target="_blank" )
        #print company

    #print num
    print  'Ok!'
    #csvfile.close()
    f.close()


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