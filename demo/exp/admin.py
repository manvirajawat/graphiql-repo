"""
Admin for demo project.
Register models in admin of demo project.
"""

from django.contrib import admin
from exp.models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
