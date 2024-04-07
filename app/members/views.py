from django.http import HttpResponse
from django.template import loader 
from django.shortcuts import render 
from json import dumps

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


def main(request): 
  template = loader.get_template('main.html')
  context = {
    }
  return HttpResponse(template.render(context, request))