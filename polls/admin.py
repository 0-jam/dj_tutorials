from django.contrib import admin
# 管理者ページからQuestionモデルにアクセスできるようにする
from .models import Question, Choice


# 選択肢テーブル登録用のフィールド
# StackedInlineを呼んでもいいが、こちらのほうがコンパクトだし、削除もできるようになる
class ChoiceInline(admin.TabularInline):
    model = Choice
    # 3つ追加できる欄をはじめから用意しておく（この欄は削除できない）
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 作成・編集フォームの入力エリアの並び順
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]

    # リストに表示したい項目を設定
    # default: __str__()
    # メソッドも指定できる（ここではwas_published_recently）
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # フィルターサイドバー
    list_filter = ['pub_date']
    # 検索フィールド
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# Choiceは以下のようにしても編集できるがわかりづらい
# admin.site.register(Choice)

# Register your models here.
