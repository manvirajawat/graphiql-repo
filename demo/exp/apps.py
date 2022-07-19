"""
AppConfig for exp app in demo project.
"""

from django.apps import AppConfig

class ExpConfig(AppConfig):
    """
    define app name and its configrations.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exp'
