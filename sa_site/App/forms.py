#!/usr/bin/env python
# encoding: utf-8
'''
@author: 
@file: forms.py
@time: 2020/10/4 下午1:21
@desc:
'''
from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, required=True, error_messages={
        'required': '必须输入名字',
        'min_length': '名字需不小于3个字符',
    })

    # email = forms.EmailField(required=True, error_messages={
    #     'required': '必须输入邮箱',
    # })

    password = forms.CharField(min_length=6, required=True, error_messages={
        'required': '必须设置密码',
        'min_length': '密码最少6位',
    })

    confirm = forms.CharField(min_length=6, required=True, error_messages={
        'required': '必须设置密码',
        'min_length': '密码最少6位',
    })

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and password.isdigit():
            raise ValidationError('密码不能是纯数字')
        return password

    def clean(self):
        password = self.cleaned_data.get('password', None)
        confirm = self.cleaned_data.get('confirm', None)
        if password != confirm:
            raise ValidationError({'confirm': '两次密码输入不一致'})
        return self.cleaned_data


class LoginForm(forms.Form):
    captcha = CaptchaField()