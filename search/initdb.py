# -*- coding: utf-8 -*-
from search.wsgi import *
from mysearch.models import Person, KeyList
#import os

def create(cnt):
	infile = "../src/result/" + str(cnt) + ".txt"
	fp = open(infile, 'r')
	title = fp.readline()
	title = title.strip()
	body = fp.read()
	body = body.strip()
	fp.close()

	people, created = Person.objects.get_or_create(identity = cnt)
	people.content = body
	people.name = title

	lines = body.split("|")
	for line in lines:
		if line is None:
			continue
		temp = line.split(":")
		key = temp[0].strip()
		if key == "Born":
			people.born = temp[1]
		if key == "Nationality":
			people.nationality = temp[1]
		if key == "Occupation":
			people.occupation = temp[1]
            

	imgUrl = "static/images/" + str(cnt) + ".jpg"
	if not os.path.exists(imgUrl):
		imgUrl = ""
	else:
		imgUrl = "images/" + str(cnt) + ".jpg"
	people.imgurl = imgUrl
	people.save()

def create_list():
	fp = open("list.txt", 'r')
	while True:
		word = fp.readline()
		word = word.strip()
		if not word:
			break
		time = fp.readline()
		time = time.strip()
		KeyList.objects.create(key = word, list = time)



def main():
	for i in range(1, 10001):
		create(i)
	create_list()

if __name__ == "__main__":
	main()
