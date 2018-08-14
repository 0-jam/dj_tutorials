from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

## pollsアプリケーション（Railsでいうコントローラー）のindexアクション
def index(request):
    # テキストを表示
    return HttpResponse("Hello, world. You're at the polls index.")
