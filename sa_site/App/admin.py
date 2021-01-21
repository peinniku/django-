from django.contrib import admin

# Register your models here.
from App.models import User, Article, Category


class UserAdmin(admin.ModelAdmin):
    list_display = ['uid', 'username', 'email', 'date_joined']
    search_fields = ['username']
    list_per_page = 5
    list_filter = ['is_superuser']

    fieldsets = [
        ('基本信息', {'fields': ['username']}),
        ('其他信息', {'fields': ['password']})

    ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['aid', 'title', 'author', 'date', 'cid_id']
    list_per_page = 5




admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
