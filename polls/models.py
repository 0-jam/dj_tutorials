# Railsでいうモデル＋マイグレーション
# 以下を実行するとDBにテーブルが登録される
# $ python manage.py migrate

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

# 投票項目
# $ rails g model question question_text:string pub_date:datetime
# 以下のようにするとレコードを作成できる
# Railsの`q = Question.create(question_text: "What's new?", pub_date: Time.current)`に相当
# q = Question(question_text="What's new?", pub_date=timezone.now())
# q.save()
# save()後は以下のようにするとカラムを確認できる（id以外のカラムも同様、Railsと同じ書式）
# q.id
# 以下のようにするとカラムを変更できる
# Railsの`q.update(question_text: "What's up?")`に相当
# q.question_text="What's up?"
# q.save()
# こんな感じで検索できる
# Railsの`Question.where(id: 1)`に相当
# Question.objects.filter(id=1)
# 以下のようにするとオブジェクトそのものを持ってこられる
# Railsの`find_by(id: 1)`と違い、条件に合うオブジェクトが2つ以上あるとエラーになる（IDでないものを探すときに注意）
# Question.objects.get(id=1)
# もちろんID以外も検索できる
# Question.objects.filter(question_text__startswith='What')
# 戻り値：<QuerySet [<Question: What's up?>, <Question: What's new?>]>


class Question(models.Model):
    # 質問事項
    # バリデーションに必要な最大文字数もここで設定できる
    # Railsの`validates :question_text, length: { maximum: 200 }`に相当
    question_text = models.CharField(max_length=200)
    # 公開日
    pub_date = models.DateTimeField('date published')

    # インスタンスメソッド
    def __str__(self):
        return self.question_text

    # 直近1日以内に作られたレコードか？
    # created_atみたいなので代用できないのかな？
    # 使用例
    # q = Question.objects.get(id=1)
    # q.was_published_recently()
    def was_published_recently(self):
        now = timezone.now()

        # pub_dateが1日以内かつ今より過去に作られた場合にTrue
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # 管理画面用設定
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# 選択肢
# $ rails g model choice question:references choice_text:string votes:integer
# ある質問事項qに関連した選択肢を取得するときは下のようにする
# Railsの`q.choices`に相当
# count()やfirst()なども実行できる
# q = Question.objects.get(id=1)
# q.choice_set.all()
# qに関連した選択肢cを作るときは下のようにする
# チュートリアルではここで`votes=0`も同時に入力しているが、デフォルトで設定されているので必要ない
# Railsの`q.choices.create(choice_text: "Just hacking again")`に相当
# c = q.choice_set.create(choice_text="Just hacking again")
# ある条件に合致したレコードを消したいときは
# c = Choice.objects.filter(choice_text__startswith="Just hacking")
# c.delete()
# 今年に作成された質問事項に関連した選択肢を抽出
# Choice.objects.filter(question__pub_date__year=current_year)


class Choice(models.Model):
    # 外部キー（Railsの`belongs_to: questions`に相当）
    # models.CASCADE：Railsの`dependent: :delete(_all)`に相当
    # 親のレコードが削除されたとき、子のレコードもすべて削除される
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # デフォルト値もここで設定できていい感じ
    votes = models.IntegerField(default=0)

    # モデルメソッド
    def __str__(self):
        return self.choice_text
