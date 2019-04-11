from django.urls import path
from . import views

# 名前空間設定
app_name = 'polls'
urlpatterns = [
    # path(`root/polls/`からみたパス, views.アクション名, name=アクション名)
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/5/
    # 汎用ビューを使う時は、URLから表示したいモデルのプライマリキーを`pk`という名前で渡す
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
