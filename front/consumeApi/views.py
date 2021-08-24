from django.shortcuts import redirect, render
import requests


def home(request, number_page: int):
    req = requests.get(f'http://localhost:8080/users/page/{number_page}')
    response = req.json()
    last_page = response['total_pages'] - 1
    return render(request, 'index.html', {'users': response['items'], 'next_page': response['next_page'], 'previous_page': response['previous_page'], 'total_pages': response['total_pages'], 'last_page': last_page})
