from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import PeopleModel

import random

import json


def getRandomChar():
    s = "qwertyuiopasdfghjklzxcvbnm"
    r = int(random.random() * 1000) % len(s)
    return s[r]

def getRandomString():
    r = int(random.random() * 1000) % 15 + 5
    s = ""
    for i in range(0,r):
        s = s + getRandomChar()
    return s



def title_page_my(request):
    return render(request, 'prilogenie111/title_page_my.html', {})

def add_people_to_table(request):
    print(request.get_full_path)
    n = 500
    for i in range(0,n):
        man_name = getRandomString()
        man_sername = getRandomString()
        man_age = int(random.random() * 1000) % 50 + 5
        PeopleModel.objects.create(man_name=man_name, man_sername=man_sername, man_age=man_age)
    return HttpResponse(str("ADDING_PEOPLE_OK"))

def add_one_man(request):
    print(request.get_full_path)
    man_name = str(request.POST['x'])
    man_sername = str(request.POST['y'])
    man_age = int(request.POST['z'])
    PeopleModel.objects.create(man_name=man_name, man_sername=man_sername, man_age=man_age)
    return HttpResponseRedirect("/" + str("?result=add_one_man_complete"))


#####################################################################################


class man:
    def setValues(self, man_name, man_sername, man_age):
        self.man_name = man_name
        self.man_sername = man_sername
        self.man_age = man_age


def jsonDefault(object):
    return object.__dict__



def get_people(request):
    print(request.get_full_path)
    v = int(request.GET['v'])
    my_records_arr = PeopleModel.objects.filter(man_age__gte=v).order_by('pk')

    answer_arr = []
    for element in my_records_arr:
        answer_arr.append(man())

    i = 0
    for element in my_records_arr:
        answer_arr[i].setValues(element.man_name, element.man_sername, element.man_age)
        print(str(i) + ")  " + element.man_name + "  " + element.man_sername + "  " + str(element.man_age))
        i = i + 1

    s = json.dumps(answer_arr, default=jsonDefault)
    return HttpResponse(str(s))


# gunicorn pg_test_dajng.wsgi