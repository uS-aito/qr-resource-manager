from django.shortcuts import render
from django.http import HttpResponse

import os
import django_filters
from rest_framework import viewsets, filters

from .models import Book
from .serializer import BookSerializer

# Create your views here.
def index(request):
    books = Book.objects.all().order_by('id')
    context = {
        "books": books
    }
    return render(request, "books/resources.html", context)

def info(request, resource_id):
    return HttpResponse(("リソース {} のページ。QRコードを読み込むとまずここにアクセスする <br>このページにはリソースの詳細(外観、性能、名前、予約状況等)を表示し、予約ボタンや詳細閲覧ボタン等を置く").format(resource_id))

def reserve(request, resource_id):
    response = "リソース {} の予約完了ページ。".format(resource_id)
    return HttpResponse(response)

def release(request, resource_id):
    return HttpResponse("リソース {} の予約解放ページ".format(resource_id))

def detail(request, resource_id):
    book = Book.objects.get(id=resource_id)
    context = book
    import pdb; pdb.set_trace()
    return render(request, "books/detail.html", context)

# REST Framework Viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer