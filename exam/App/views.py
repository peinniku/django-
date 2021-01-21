from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import User


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', context={'title': 'django', 'name': '用戶', 'users': users})
    # return HttpResponse('首頁')


def get_name(request, name):
    print(request.GET)
    print(request.GET.getlist('age'))
    return HttpResponse(name)


def http_redirect(request):
    return redirect(reverse('tel', args=('1234-56795978',)))


def tel(request, phone):
    return HttpResponse(phone)
