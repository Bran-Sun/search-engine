import urllib2
import urllib
import re
import os
import sys
from bs4 import BeautifulSoup

def getInfo(filename, cnt):
	fp = open(filename, 'r')
	#title = fp.readline()
	html = fp.read()
	fp.close()
	outfile = "src/result/" + str(cnt) + ".txt"
	fw = open(outfile, 'w')
	info = BeautifulSoup(html, "lxml")
	trList = info.find_all("tr")
	cnt = 0
	#fw.write(title)
	for tr in trList:
		fout = ''
		cnt = cnt + 1
		content = False
		head = 0
		if (cnt > 1):
			tag = ""
			for string in tr.stripped_strings:
				if head == 0:
					tag = string.encode('utf-8')
					fout = fout + string.encode('utf-8') + ":"
				else:
					temp = string.strip()
					start = temp.find("(")
					if start != -1:
						temp = temp[:start] + temp[start + 1 : ]
					end = temp.find(")")
					if end == len(temp) - 1:
						temp = temp[: -1]
					start = temp.find(",")
					if start == 0:
						temp = temp[1:]
					end = temp.find(",")
					if end == len(temp) - 1:
						temp = temp[: -1]
					if temp == "[1]" or temp == "[2]" or temp == "[3]" or temp == "[4]" or temp == "[5]" or temp == "[6]" or temp == "[7]" or temp == "[8]" or temp == "[9]":
						temp = ""
					if temp == "":
						head = head + 1
						continue
					if (tag == "Born") and (head == 1):
						if not temp[0].isdigit():
							head = head + 1
							continue
					if temp !="":
						fout = fout + temp.encode('utf-8') + ";"
						content = True
				head = head + 1
		else:
			label = True
			for title in tr.stripped_strings:
				if label:
					fw.write(title.encode('utf-8') + "\n")
					label = False
				else:
					break
		if content:
			fw.write(fout + "|\n")
	fw.close()

def main():
	for i in range(1, 10001):
		filename = "src/doc/" + str(i) + ".html"
		getInfo(filename, i)

if __name__ == "__main__":
	main()