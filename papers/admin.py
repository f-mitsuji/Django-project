from django.contrib import admin

from .models import Comment, Paper

admin.site.register(Paper)
admin.site.register(Comment)
