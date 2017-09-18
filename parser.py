#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import re
import os
import sys
from bs4 import BeautifulSoup

class Parser:
	"parser"

	def __init__(self, url):
		self.url = url
		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		self.headers = { 'User-Agent' : self.user_agent }
		self.id = 8636
		self.dic = {}

	def getMessage(self):
		self.getUrls2()
		cnt = 0
		for url in self.next:
			print(str(cnt) + "  " + str(self.id))
			print(url)
			self.getInfo(url)
			cnt = cnt + 1

	def getUrls(self):
		request = urllib2.Request(self.url,headers = self.headers)
		response = urllib2.urlopen(request)
		html = response.read()
		soup = BeautifulSoup(html, "lxml")

		self.next = []
		list = soup.find_all("span", class_ = "fn")
		leng = len(list)
		start = self.id + 15
		for i in range(start, leng):
			url = list[i].contents[0].get('href')
			self.next.append("https://en.wikipedia.org" + url)

	def getUrls2(self):
		request = urllib2.Request(self.url,headers = self.headers)
		response = urllib2.urlopen(request)
		html = response.read()
		soup = BeautifulSoup(html, "lxml")

		list = soup.find_all("a")
		leng = len(list)
		start = 0
		self.next = []
		for i in range(start, leng):
			url = list[i].get('href')
			if url is None:
				continue
			if url[0 : 5] != '/wiki':
				continue
			#print(url)
			self.next.append("https://en.wikipedia.org" + url)

	def getInfo(self, url):
		#print(self.id)
		request = urllib2.Request(url,headers = self.headers)
		response = urllib2.urlopen(request)
		html = response.read()
		soup = BeautifulSoup(html, "lxml")
		'''infolist = soup.find_all("table", class_ = "infobox biography vcard")
		if len(infolist) == 0:
			infolist = soup.find_all("table", class_ = "infobox vcard")
		if len(infolist) == 0:
			infolist = soup.find_all("table", class_ = "infobox vcard plainlist")
		if len(infolist) == 0:
			infolist = soup.find_all("table", class_ = "infobox border vcard")
		if len(infolist) == 0:
			infolist = soup.find_all("table", class_ = "infobox")
		if len(infolist) == 0:
			infolist = soup.find_all("table", class_ = "infobox")
		if len(infolist) == 0:
			return
		info = infolist[0]'''
		start = html.find(r'<table class="infobox')
		if start == -1:
			return
		end = html.find(r'</table>', start) + 8
		info = html[start : end]

		infosoup = BeautifulSoup(info, "lxml")
		#print(infosoup)

		fp = open("src/doc/%s.txt" % self.id, 'w')
		titleList = infosoup.find_all("th")
		if len(titleList) == 0:
			fp.close()
			return
		title = titleList[0].string
		if title is None:
			fp.close()
			return
		fp.write(title.encode('utf-8') + "\n")

		imglist = infosoup.find_all('img')
		if len(imglist) != 0:
			imgurl = "https:" + imglist[0].attrs['src']
			urllib.urlretrieve(imgurl,'src/img/%s.jpg' % self.id)
 	
 		infoout = infosoup.find_all("table")[0]
		fp.write(infoout.encode('utf-8'))
		'''trList = info.find_all("tr")
		cnt = 0
		for tr in trList:
			cnt = cnt + 1
			head = True
			if (cnt > 1):
				for string in tr.stripped_strings:
					if head:
						fp.write(string.encode('utf-8') + " : ")
						head = False
					else:
						fp.write(string.encode('utf-8') + "; ")
				fp.write("\n")'''
		self.id = self.id + 1
		fp.close();
				








