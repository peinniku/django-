#!/usr/bin/env python
# encoding: utf-8
'''
@author: 
@file: MyMiddleware.py
@time: 2020/12/4 下午7:43
@desc:
'''
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            return
        else:
            return HttpResponse('hello')
