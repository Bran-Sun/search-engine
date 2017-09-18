# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Person, KeyList

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):	
	return render(request, 'search_form.html')

def result(request):
    message = request.GET['q']
    queslist = message.split(" ")
    nationality = request.GET['nationality']
    born = request.GET['born']
    occupation = request.GET['occupation']

    mother = []
    satispeople = Person.objects.filter(born__contains=born).filter(nationality__contains=nationality).filter(occupation__contains=occupation)
    for people in satispeople:
        mother.append(people.identity)

    quescnt = len(queslist)
    l = [[] for i in range(quescnt)]

    for ques in queslist:
        try:
            word = KeyList.objects.get(key = ques)
            identitys = word.list
            idlist = identitys.split(" ")
            for identiti in idlist:
                exist = False
                for i in range(quescnt - 1):
                    if identiti in l[i]:
                        l[i].remove(identiti)
                        l[i + 1].append(identiti)
                        exist = True
                        break
                if not exist:
                    l[0].append(identiti)
        except ObjectDoesNotExist:
            continue

    persons = []
    for li in l:
        for item in li:
            if int(item) in mother:
                persons.append(item)
    persons.reverse()

    if len(message) == 0:
        persons = mother

    personlist = []
    '''for person in persons:
        info = {}
        dic = []
        m_person = Person.objects.get(identity = int(person))

        info['img'] = m_person.imgurl

        dic.append(['name', m_person.name])
        content = m_person.content
        lines = content.split("|")
        for line in lines:
            if line is None:
                continue
            temp = line.split(":")
            key = temp[0]
            if len(temp) > 1:
                dic.append([key, temp[1]])
        info['info'] = dic       
        personlist.append(info)'''

    try:  
        curPage = int(request.GET.get('curPage', '1'))  
        allPage = int(request.GET.get('allPage','1'))  
        pageType = str(request.GET.get('pageType', ''))  
    except ValueError:  
        curPage = 1  
        allPage = 1  
        pageType = ''  
  
    #判断点击了【下一页】还是【上一页】  
    if pageType == 'pageDown':  
        curPage += 1  
    elif pageType == 'pageUp':  
        curPage -= 1 
    ONE_PAGE_OF_DATA = 10 
  
    startPos = (curPage - 1) * ONE_PAGE_OF_DATA  
    endPos = startPos + ONE_PAGE_OF_DATA

    personpage = persons[startPos:endPos] 

    cnt = 0
    for person in personpage:
        m_person = Person.objects.get(identity = int(person))
        info = {}
        info['label'] = cnt % 2
        info['name'] = m_person.name
        info['id'] = m_person.identity
        info['img'] = m_person.imgurl

        content = m_person.content
        lines = content.split("|")
        for line in lines:
            if line is None:
                continue
            temp = line.split(":")
            key = temp[0].strip()
            if key == "Born":
                info['Born'] = temp[1]
            if key == "Died":
                info['Died'] = temp[1]


        personlist.append(info) 
        cnt = cnt + 1
  
    if curPage == 1 and allPage == 1: #标记1  
        allPostCounts = len(persons)  
        allPage = allPostCounts / ONE_PAGE_OF_DATA  
        remainPost = allPostCounts % ONE_PAGE_OF_DATA  
        if remainPost > 0:  
            allPage += 1  

    return render(request, 'result.html', {'nationality' : nationality,'born' : born, 'occupation' :occupation,'message' : message, 'PersonList' : personlist, 'allPage':allPage, 'curPage':curPage})
    #return render(request, 'result.html', { 'Hello' : message})

def person(request, m_id):
    m_person = Person.objects.get(identity = int(m_id))
    info = {}
    info['img'] = m_person.imgurl
    dic = []

    dic.append(['name', m_person.name])
    content = m_person.content
    lines = content.split("|")
    for line in lines:
        if line is None:
            continue
        temp = line.split(":")
        key = temp[0]
        if len(temp) > 1:
            dic.append([key, temp[1]])
    info['info'] =  dic   
    return render(request, 'person.html', {'person' : info})




