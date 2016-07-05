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

if __name__ == "__main__":
#从a.txt中找出相应字段，写入b.txt中 
    atitle = [ ]
    area1=[]
    area2=[]
    file_object_Z  =open ('sogou.dat','r') 
    #    with open ('result1.csv','w') as f2:
    key1=re.compile('html" title="(.*?)">')  #正则内容
    key2=re.compile('districtName="(.*?)" plateName="(.*?)"')
    key3=re.compile('plateName="(.*?)"')
    
    for i in file_object_Z :
        value=re.search(key1,i)
        if value:
            atitle.append(value.group(1).decode('utf-8'))
           # print value.group(1)


    file_object_Z  =open ('sogou.dat','r')     
    for i in file_object_Z:
        value2=re.search(key2,i)
        if value2:
             area1.append(value2.group(1).decode('utf-8'))
             
             

    file_object_Z  =open ('sogou.dat','r')          
    for i in file_object_Z:
        value3=re.search(key3,i)
        if value3:
            area2.append(value3.group(1).decode('utf-8'))
        #    print value3.group(1)
  
    
    csvfile = file('result.csv', 'w')
    csvfile.write('\xEF\xBB\xBF'); 
    writer = csv.writer(csvfile)
    writer.writerow([u'小区',u'区域1',u'区域2'])

    if len(atitle) > len(area2):
        for i in range(len(atitle) - len(area2)):
            area2.append('---')

    if len(atitle) > len(area1):
        for i in range(len(atitle) - len(area1)):
            area1.append('---')

    for i in range(len(atitle)):
            message = atitle[i]+'|'+area1[i]+'|'+area2[i]
            #    + '|'+afixedprice[i]+'|'+ adate[i]
            writer.writerow([i for i in str(message).split('|')])
    print "[Result]:> 页面信息保存完毕!"
    csvfile.close()
           # f2.write(codecs.BOM_UTF8)    #csv识别utf8格式
           # f2.write(value.group(1).strip()+'\r')   #结果换行输出


'''         
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
'''

