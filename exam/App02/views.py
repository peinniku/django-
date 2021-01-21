from datetime import datetime
from random import randint

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App02.models import User


def index(request):
    users = [{'username': 'pein'}, {'username': 'niku'}]
    return render(request, 'app02/index.html', context=locals())


def fil(request):
    num = 9
    var = None
    t1 = datetime.now()
    return render(request, 'test.html', context=locals())


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
    return render(request, 'app02/register.html')


def include_url(request):
    return render(request, 'app02/menu.html')


def handle_data(request):
    # user = User(username='pein', password='150620')
    # user.save()
    # User.objects.create(username='ert',password='12345678')
    # User.objects.bulk_create([User(username='ad1', password='pw1'), User(username='ad2', password='pw2')])

    # user1 = User.objects.get(pk=5)
    # user.password = 'abcd1234'
    # user.save()
    # users = User.objects.filter(uid__gte=1)
    # print(users)
    # users.delete()
    # print(user, type(user))
    # if user:
    #     user.delete()

    first_name = ['王', '李', '张', '刘', '陈', '杨', '黄', '赵', '吴', '周']
    last_name = ['俊豪', '婉如', '嘉美', '子轩', '志妍', '山勇', '秀法']
    users = []
    for first in first_name:
        for last in last_name:
            name = first + last
            users.append(User(username=name, password=randint(11111111, 99999999)))

    User.objects.bulk_create(users)

    return HttpResponse('数据添加完毕')


def search(request):
    # data = User.objects.all()
    # data = User.objects.filter(uid__gt=40).filter(uid__lt=50)
    # data = User.objects.order_by('uid')[20:30]
    # data = User.objects.filter(username__startswith='张')

    # from django.db.models import Max,Min,Sum,Avg
    # uid = User.objects.aggregate(
    #
    #
    # Max('uid'))
    # print(uid)
    # return HttpResponse('分组排序')

    data = User.objects.filter(Q(uid__lte=12) | Q(uid__gte=70))
    return render(request, 'app02/list.html', locals())


def send(request):
    from App02.sms import send_sms
    mobile = "18981200020"
    text = "您的验证码是：121254。请不要把验证码泄露给其他人。"
    print(send_sms(text, mobile))
    return HttpResponse('发送成功')


def show_page(request,page_num=1):
    users = User.objects.all()
    paginator = Paginator(users,10)
    pages = paginator.page(page_num)
    last_page = -paginator.num_pages
    print(last_page)
    return render(request, 'app02/page.html',locals())


