"""
Creating models Post and Comment.
"""

from django.db import models

class Post(models.Model):
    """
    Parameters
    ----------
    created_on for timestamp
    title for post titile
    text for post description
    """
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()

class Comment(models.Model):
    """
    Parameters
    ----------
    created_on
    author_name
    author_email
    text
    """
    created_on = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField()
    text = models.TextField()
