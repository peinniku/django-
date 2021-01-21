from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Category(models.Model):
    cid = models.AutoField(primary_key=True, )
    cname = models.CharField(max_length=30)

    class Meta:
        db_table = 'category'
        # managed = False
        # ordering = ['regtime']


class Article(models.Model):
    aid = models.AutoField(primary_key=True)
    cid = models.ForeignKey(to='Category', to_field='cid', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    context = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # managed = False
        db_table = 'article_table'

    def cid_id(self):
        if self.cid == '1':
            return '学习'
        elif self.cid == '2':
            return '电影'
        elif self.cid == 3:
            return '游戏'
        elif self.cid == 4:
            return '杂谈'


class User(AbstractUser):
    uid = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30, unique=True,verbose_name='用户名')
    password = models.CharField(max_length=100)
    regtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        ordering = ['regtime']
