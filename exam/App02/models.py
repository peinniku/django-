from django.db import models


# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    regtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
        ordering = ['regtime']
