from django.http import HttpResponse
from django.template import loader 

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def eureka(request): 
  template = loader.get_template('eureka.html')
  return HttpResponse(template.render())

def events(request): 
  template = loader.get_template('events.html')
  return HttpResponse(template.render())