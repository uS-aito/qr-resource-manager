from django.shortcuts import render
from django.http import HttpResponse

import os

# Create your views here.
def index(request):
    return HttpResponse("Hello, World.")

def info(request, resource_id):
    return HttpResponse(("リソース {} のページ。QRコードを読み込むとまずここにアクセスする <br>このページにはリソースの詳細(外観、性能、名前、予約状況等)を表示し、予約ボタンや詳細閲覧ボタン等を置く").format(resource_id))

def reserve(request, resource_id):
    response = "リソース {} の予約完了ページ。".format(resource_id)
    return HttpResponse(response)

def release(request, resource_id):
    return HttpResponse("リソース {} の予約解放ページ".format(resource_id))