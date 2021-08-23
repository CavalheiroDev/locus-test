from django.shortcuts import render
import requests


def home(request):
    response = requests.get('http://localhost:8080/users/page/1')
    users = response.json()
    return render(request, 'consumeApi/home.html', {'users': users})
