from django.http import HttpResponse
from django.template import loader 
from django.shortcuts import render, redirect
from django.contrib import messages
from pymongo import MongoClient
from .models import User

from json import dumps

def connect_to_mongodb():
    client = MongoClient('mongodb+srv://nottherealericl:r6SZdtENM5ms3TvP@cluster0.wnrccgr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['eureka']
    return db
  
def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def eureka(request): 
  template = loader.get_template('eureka.html')
  
  return render(request, 'eureka.html') 

def send_dictionary(request): 
    # create data dictionary 
    dataDictionary = { 
        'hello': 'World', 
        'geeks': 'forgeeks', 
        'ABC': 123, 
        456: 'abc', 
        14000605: 1, 
        'list': ['geeks', 4, 'geeks'], 
        'dictionary': {'you': 'can', 'send': 'anything', 3: 1} 
    } 
    # dump data 
    dataJSON = dumps(dataDictionary) 
    return render(request, 'landing.html', {'data': dataJSON}) 

def events(request): 
  template = loader.get_template('events.html')
  eurekaDict = [{"id": 0, "lat": 0, "long":0}, {"id":1, "lat":1, "long":1} ]
  eurekaJSON = dumps(eurekaDict)

  context = {
    'eureka_elms': eurekaJSON
    }

  return HttpResponse(template.render(context, request))
#   return HttpResponse(template.render())


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        db = connect_to_mongodb()
        user = db.users.find_one({'email': email, 'password': password})
        if user:

            return redirect('events')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        db = connect_to_mongodb()
        if db.users.find_one({'email': email}):
            messages.error(request, 'Email already exists.')
        else:
            db.users.insert_one({'name': name, 'email': email, 'password': password})
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    return render(request, 'signup.html')
