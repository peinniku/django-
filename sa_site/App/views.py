import json
import os

from datetime import datetime, timedelta

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.forms import RegisterForm, LoginForm
from App.models import Category, Article, User
from sa_site import settings


def check_login(func):
    def inneer(*args, **kwargs):
        if args[0].session.get('username'):
            return func(*args, **kwargs)
        else:
            return redirect('App:login')

    return inneer


def index(request):
    # username = request.COOKIES.get('username')

    trans_username = request.session.get('username')
    # if username:
    #     trans_username = json.loads(username)
    return render(request, 'index.html', locals())


# @check_login
@login_required(login_url='/login/')
def article(request, cid=-1):
    categories = Category.objects.all()
    if cid < 0:
        first_category = categories.first()
        cid = first_category.cid

    articles = Article.objects.filter(cid=cid)
    # username = request.COOKIES.get('username')
    # trans_username = request.session.get('username')
    # if username:
    #     trans_username = json.loads(username)
    return render(request, 'table-datatable.html', locals())


def edit(request, aid):
    art = Article.objects.filter(aid=aid).first()
    if request.method == 'POST':
        con = request.POST.get('content')
        art.context = con
        art.save()
    return render(request, 'ariticle-editor.html', locals())


# def login(request):
#     if request.method == 'POST':
#         userinfo = request.POST.dict()
#         userinfo.pop('csrfmiddlewaretoken')
#         user = User.objects.filter(**userinfo).first()
#         # print(user.username)
#         # user.username = user.username.encode('utf-8')
#
#         if user:
#             response = redirect('App02:index')
#             # future = datetime.now() + timedelta(days=3)
#             # response.set_cookie('username', json.dumps(user.username), expires=future)
#
#             request.session['username'] = user.username
#             request.session['uid'] = user.uid
#
#             return response
#     return render(request, 'page-login.html')


# def logout(request):
#     res = redirect('App:index')
#     # res.delete_cookie('username')
#
#     request.session.flush()
#     return res


#
# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#
#         if form.is_valid():
#             data = form.cleaned_data
#             data.pop('confirm')
#             print(data)
#             res = User.objects.create(**data)
#
#
#         else:
#             return render(request, 'page-register.html', locals())
#             # return HttpResponse('有错误')
#     return render(request, 'page-register.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            data.pop('confirm')
            print(data)
            res = User.objects.create_user(**data)

        else:
            return render(request, 'page-register.html', locals())
    return render(request, 'page-register.html')


def auth_login(request):
    form = LoginForm()
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        form = LoginForm(request.POST)
        if form.is_valid():
            if user:
                login(request, user)
                response = redirect('App:index')
                # future = datetime.now() + timedelta(days=3)
                # response.set_cookie('username', json.dumps(user.username), expires=future)
                return response
            else:
                msg = '用户名或密码错误'
                return render(request, 'page-login.html', locals())
        else:
            msg = '图形验证码出错'
            return render(request, 'page-login.html', locals())

    return render(request, 'page-login.html', locals())


def auth_logout(request):
    res = redirect('App:index')
    # res.delete_cookie('username')
    logout(request)
    return res


def upload(request):
    if request.method == 'POST':
        fobj = request.FILES.get('photo')
        path = os.path.join(settings.STATICFILES_DIRS[0], 'upload')
        path = os.path.join(path, fobj.name)
        if fobj:
            print(fobj.name, fobj.size, )
            with open(path, 'wb') as target:
                if fobj.multiple_chunks():
                    for data in fobj.chunks():
                        target.write(data)
                else:
                    target.write(fobj.read())

    return render(request, 'file-upload.html', locals())


def header(request):
    return render(request, 'header.html')
