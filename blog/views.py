from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .tasks import execute_cmd
from django.views.decorators.csrf import csrf_exempt
import requests
import socket

# views.py 상에서의 request 실습 예제


@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html', {'GET': 'GET!'})
    if request.method == 'POST':
        execute_cmd.apply_async(countdown=2)
        i = request.POST['search']
        response = requests.get('http://' + socket.gethostbyname(socket.gethostname()) + ':8000/wow', params={'id': i}, verify=False)

        ans = response.json()
        return render(request, 'home.html', {'POST': ans['key']})


@csrf_exempt
def wow(request):
    if request.method == 'GET':
        i = request.GET['id']
        i += ' fucking good'

        return JsonResponse({'key': i})

    return HttpResponse()
