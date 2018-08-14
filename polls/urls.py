from django.urls import path
from . import views

# 名前空間設定
app_name = 'polls'
urlpatterns = [
    # path(`root/polls/`からみたパス, views.アクション名, name=アクション名)
    # /polls/
    path('', views.index, name='index'),
    # /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
