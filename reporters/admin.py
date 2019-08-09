from django.contrib import admin
from .models import Reporter, Article, Category

# Register your models here.
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Category)
