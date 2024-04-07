from django.http import HttpResponse
from django.utils.http import urlencode
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
  db = connect_to_mongodb()

  eurekaDB = db.locations
  eurekaDict = []
  for entry in eurekaDB.find():
      processed = dict((k,entry[k]) for k in 
           ("id", "activity_name", "location_name", "address", "latitude", "longitude", "rewarded_pet_type_id", "category") if k in entry)
      processed["start_time"] = entry['start_time'].strftime("%Y-%m-%dT%H:%M")
      processed["end_time"] = entry['end_time'].strftime("%Y-%m-%dT%H:%M")
      processed["maps_link"] = 'https://www.google.com/maps/place/' + entry['address'].replace(" ", "+")
      eurekaDict.append(processed)

#   eurekaDict = [{"id": 0, "lat": 0, "long":0}, {"id":1, "lat":1, "long":1} ]
  eurekaJSON = dumps(eurekaDict)

  context = {
    'eureka_elms': eurekaJSON,
    'eureka_dict': eurekaDict
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

#specific page
def eureka2(request, id): 
    template = loader.get_template('eureka_deets.html')
    
    eurekaDict = [{"id": 0, "lat": 0, "long":0}, {"id":1, "lat":1, "long":1} ]

    eurekaJSON = dumps(eurekaDict)

    context = {
    'eureka_info': eurekaJSON
    }

    return HttpResponse(template.render(context, request))
