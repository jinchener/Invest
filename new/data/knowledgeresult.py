#!/usr/bin/python26
# -*- coding: utf-8 -*- 
import sys
import os
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re
import glob
import csv
import codecs 


#从a.txt中找出相应字段，写入b.txt中 

with open ('sogou.dat','r') as f:
 with open ('result1.csv','w') as f2:
    key=re.compile('html" title="(.*?)">')  #正则内容
    for i in f:
        value=re.search(key,i)
        if value:
            f2.write(codecs.BOM_UTF8)    #csv识别utf8格式
            f2.write(value.group(1).strip()+'\r')   #结果换行输出
           
with open ('sogou.dat','r') as f:
 with open ('result2.csv','w') as f2:
    key=re.compile('districtName="(.*?)" plateName="(.*?)"')
    for i in f:
        value=re.search(key,i)
        if value:
            f2.write(codecs.BOM_UTF8)
            f2.write(value.group(1).strip()+'\r')

with open ('sogou.dat','r') as f:
 with open ('result3.csv','w') as f2:
    key=re.compile('plateName="(.*?)"')
    for i in f:
        value=re.search(key,i)
        if value:
            f2.write(codecs.BOM_UTF8)
            f2.write(value.group(1).strip()+'\r')


