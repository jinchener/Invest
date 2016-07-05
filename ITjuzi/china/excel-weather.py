import os
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
import datetime
import time

ltime=time.time()-86400*2
timeStr=time.strftime("%Y-%m-%d", time.localtime(ltime))
url="http://wsbs.bjepb.gov.cn/air2008/Air1.aspx?time="
url=url+timeStr
req = urllib2.Request(url)
res = urllib2.urlopen(req)
html = res.read()
soup= BeautifulSoup(html)

trs=soup.find("table",id="DaliyReportControl1_DataGridDataDic")
length=len(trs.contents)
for x in range(2,length-1):
    print trs.contents[x].contents[2].string
    print trs.contents[x].contents[3].string
    print trs.contents[x].contents[4].string
    print trs.contents[x].contents[5].string