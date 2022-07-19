"""
Creating indexView for crud operations and render to an index.html page.
"""

# from turtle import title
from django.shortcuts import render
from exp.models import Post

# Create your views here.
def index_view(request):
    """
    Perform CRUD operations using ORM and render to html page.
    """
    # Post.objects.create(title="abc", text="abc abc")
    # deldata = Post.objects.get(id=4)
    # deldata.delete()
    # Post.objects.filter(title="aaa").delete()
    Post.objects.filter(title="mysql").update(text="mysql database")
    # result = Post.objects.filter(title="mysql")
    result = Post.objects.all()
    print(result)
    return render(request, "index.html")
