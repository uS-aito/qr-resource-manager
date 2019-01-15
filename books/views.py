from django.shortcuts import render
from django.http import HttpResponse

import os
import django_filters
from rest_framework import viewsets, filters

from .models import Book
from .serializer import BookSerializer

# Create your views here.
def index(request, **kwargs):
    if "resource_type" in kwargs.keys():
        # 指定されたクラスの動的な読み込み
        # https://docs.python.org/3.6/library/functions.html#__import__
        # https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class
        ## 指定されたクラスのみを読み込み
        mod = __import__("books.models", globals(), locals(), [kwargs["resource_type"]], 0)
        resource_class = getattr(mod, kwargs["resource_type"])
        ## そのクラスのレコードをDBから読み込み
        resources = resource_class.objects.all().order_by("id")

        context = {
            "resources": resources
        }
        return render(request, "books/resources.html", context)
    else:
        # リソースを全部読み込み
        ## modelsに定義されている全てのオブジェクトを読み込み
        mod = __import__("books.models", globals(), locals(), [], 0)
        ## 読み込んだオブジェクトのうち、リソースのクラスのみresources_allに突っ込む
        ## typeがdjango.db.models.base.ModelBaseのやつはmodels.Modelを継承している→リソースのクラス
        resources_all = []
        for name in dir(mod.models):
            attr = getattr(mod.models, name)
            if "django.db.models.base.ModelBase" in str(type(attr)):               
                resources_all.append(attr.objects.all().order_by('id'))
        context = {
            "resources_all": resources_all
        }
        return render(request, "books/resources_all.html", context)

def detail(request, **kwargs):
    # 動的なクラス読み込み
    mod = __import__("books.models", globals(), locals(), [kwargs["resource_type"]], 0)
    resource_class = getattr(mod, kwargs["resource_type"])
    # そのクラスのレコードをDBから読み込み
    resource = resource_class.objects.get(id=kwargs["resource_id"])

    context = {
        "resource": resource
    }
    return render(request, "books/detail.html", context)

# REST Framework Viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer