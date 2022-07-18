from django.db import models

class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()

class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField()
    text = models.TextField()

