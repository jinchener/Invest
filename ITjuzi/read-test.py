#!/usr/bin/python
# -*- coding:utf-8 -*-
# regex_spider.py
# author: song


import zlib
import struct
from bs4 import BeautifulSoup as bs
import traceback
import re




if __name__ == "__main__":
	#file_object_Z = open('result.txt', 'w')

	#file_object_Z = open('index.html', "rb")
	#soup = BeautifulSoup(file_object_Z.read())
	#file_object_Z = open('result.txt', 'w')	
	soup = bs(open('index.html'),"lxml")
	#for child in  soup.body.children:
	soup1=soup.find("div","main")
	print soup1.find("div","sec")
	#file_object_Z.write(soup.find_all("div","info-panel"))
	#print soup.find_all('h2')
	#for tag in soup.find_all(re.compile("^b")):
    #print(tag.name)
	#file_object_Z.close()
	
	
	'''
	try:
		for i in range(1, 2000 + 1):
			file_object = open("data/baike_%d.html"%(i), "wb")
			try:
				urlLen = struct.unpack("L",file_object_Z.read(4))
				baikeUrl = file_object_Z.read(urlLen[0])
				print baikeUrl

				nLen = file_object_Z.read(4)
				nHtmlLen = struct.unpack("L",nLen)
				baikeHtml = file_object_Z.read(nHtmlLen[0])
				file_object.write(zlib.decompress(baikeHtml))
				print "%d, Len: %d"%(i,nHtmlLen[0])
			except IOError, e:
				print "*** file write error:", e
				break
			finally:
				file_object.close()
	'''
	#finally:
		#file_object_Z.close()
	print "ok!"
