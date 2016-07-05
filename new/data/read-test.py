#!/usr/bin/python
# -*- coding:utf-8 -*-
# regex_spider.py
# author: song


import zlib
import struct
import sys
from bs4 import BeautifulSoup as bs
import traceback
import re





if __name__ == "__main__":
    #file_object_Z = open('result.txt', 'w')

    #file_object_Z = open('index.html', "rb")
    #soup = BeautifulSoup(file_object_Z.read())
    #file_object_Z = open('result.txt', 'w')
    soup = bs(open('fileappend.txt'))
    #courseInfo=soup.find(attrs={ "class": "house-lst"})
    course=soup.find_all("a","actshowMap_list")
    #print course
    for text in course:
        print(text.get('platename'))
    #print course
    #course=soup.find_all('a',"selectDetail")
    #print course
    #for text in course:
     #    print(text.get('districtname'))
    #for text in courseInfo.find_all('a'):
     #   print(text.get_text())
    #file_object_Z.write(courseInfo)
    #file_object_Z.close()
    #file_object_Z.write(soup.find_all("div","info-panel"))
    #print soup.find_all('h2')
    #for tag in soup.find_all(re.compile("^b")):
    #print(tag.name)
    #file_object_Z.close()



    #finally:
        #file_object_Z.close()
    print "ok!"