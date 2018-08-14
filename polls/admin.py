from django.contrib import admin
# 管理者ページからQuestionモデルにアクセスできるようにする
from .models import Question
admin.site.register(Question)

# Register your models here.
