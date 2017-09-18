import re
import os
import sys

dic = {}

for i in range(1, 10001):
	filename = "src/result/" + str(i) + ".txt"
	fp = open(filename, "r")

	title = fp.readline()
	body = fp.read().decode('utf-8')
	fp.close()

	body = body.strip()
	lines = body.split("\n")

	for cline in lines:
		line = cline.strip()
		line = line.strip("|")
		items = line.split(":")
		if len(items) <= 1:
			continue
		name = items[0].strip()
		attrs = items[1].split(";")
		for attr in attrs:
			words = attr.split(" ")
			for word in words:
				temp = word
				start = temp.find("(")
				if start == 0:
					temp = temp[1:]
				end = temp.find(")")
				if end == len(temp) - 1:
					temp = temp[: -1]
				start = temp.find(",")
				if start == 0:
					temp = temp[1:]
				end = temp.find(",")
				if end == len(temp) - 1:
					temp = temp[: -1]
				if (temp != " ") and (temp != ""):
					if dic.has_key(temp):
						if i in dic[temp]:
							continue
						dic[temp].append(i)
					else:
						dic[temp] = []
						dic[temp].append(i)

fw = open("list.txt", 'w')

for key, value in dic.items():
	fw.write(key.encode('utf-8') + "\n")
	for i in value:
		fw.write(str(i) + " ")
	fw.write("\n")
