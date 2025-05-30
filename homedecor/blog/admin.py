from django.contrib import admin
from .models import Article, BlogCategory, Tag

# Register your models here.
admin.site.register(Article)
admin.site.register(BlogCategory)
admin.site.register(Tag)
