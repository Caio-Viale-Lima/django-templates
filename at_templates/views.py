from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(request):

  response = requests.get('https://randomuser.me/api/')
  user = json.loads(response.text)["results"][0]


  context = {
    'username': user["login"]["username"],
    'fullname': user["name"]["first"] + " " + user["name"]["last"],
    'gender': user["gender"],
    'email': user["email"],
    'cell': user["cell"],
    'picture': user["picture"]["large"],
    'location': user["location"]["city"] + ", " + user["location"]["state"] + ", " + user["location"]["country"]
  }



  return render(request, 'at_templates/starter.html', context)