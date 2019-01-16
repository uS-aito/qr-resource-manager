from django.shortcuts import render
from django.http import HttpResponse

# import os

# 認証ページ用
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# レンタルページ用
from .forms import RentalForm

# djanog rest framework用
import django_filters
from rest_framework import viewsets, filters
from .models import Book, Monitor
from .serializer import BookSerializer, MonitorSerializer

# リソースの一覧を表示するページ
@login_required
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
            # Resourceは基底クラスなので無視する
            if name=="Resource":
                continue
            attr = getattr(mod.models, name)
            if "django.db.models.base.ModelBase" in str(type(attr)):               
                resources_all.append(attr.objects.all().order_by('id'))
        context = {
            "resources_all": resources_all
        }
        return render(request, "books/resources_all.html", context)

@login_required
def detail(request, **kwargs):

    if request.method == "POST":
        # フォーム受け取り
        form = RentalForm(request.POST)
        # 内容の検証
        if form.is_valid():
            # 動的なクラス読み込み
            mod = __import__("books.models", globals(), locals(), [kwargs["resource_type"]], 0)
            resource_class = getattr(mod, kwargs["resource_type"])
            # そのクラスのレコードをDBから読み込み
            resource = resource_class.objects.get(id=kwargs["resource_id"])
            # 利用者、貸し出し日、返却予定日を更新
            resource.checkout_date = form.cleaned_data["checkout_date"]
            resource.return_date = form.cleaned_data["return_date"]
            resource.username = request.user.username
            # 更新を保存
            resource.save()

        context = {
            "resource": resource,
            "form": form
        }

        return render(request, "books/detail.html", context)

    else:
        # 動的なクラス読み込み
        mod = __import__("books.models", globals(), locals(), [kwargs["resource_type"]], 0)
        resource_class = getattr(mod, kwargs["resource_type"])
        # そのクラスのレコードをDBから読み込み
        resource = resource_class.objects.get(id=kwargs["resource_id"])

        # レンタルページ用のformを作成
        form = RentalForm()
        
        context = {
            "resource": resource,
            "form": form
        }
        return render(request, "books/detail.html", context)

# REST Framework Viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer