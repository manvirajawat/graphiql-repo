"""
Create URL's for exp app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view)
]
