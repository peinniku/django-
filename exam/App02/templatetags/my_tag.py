#!/usr/bin/env python
# encoding: utf-8
"""
@author:
@file: my_tag.py
@time: 2020/7/5 下午6:40
@desc:
"""

from django import template

register = template.Library()


@register.filter(name='sub')
def sub(value):
    return value + 2