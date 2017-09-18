import urllib2
import urllib
import re
import os
import sys

fp = open("result.txt", "r")
title = fp.readline()
body = fp.read()
fp.close()

body = body.strip()
lines = body.split("\n")

for line in lines:
	items = line.split(":")
	name = items[0].strip()
	print(name)
	attrs = items[1].split(";")
	for attr in attrs:
		words = attr.split(" ")
		for word in words:
			if word != "":
				end = word.find(",")
				if end == len(word) - 1:
					word = word[: -1]
				print(word)