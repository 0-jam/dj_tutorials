# $ python manage.py test polls でテストを実行できる

from django.test import TestCase
from django.utils import timezone

import datetime

from .models import Question
# Create your tests here.

## テストクラスを作成
# テストメソッド名は"test"で始めなくてはいけない
class QuestionModelTests(TestCase):
    ## pub_dateが未来になっているときに「最近作られた」と誤判断されないか？
    def test_was_published_recently_with_future_question(self):
        # あるQuestionオブジェクトfuture_questionのpub_dateが未来（ここでは30日後）になっているとき、
        # future_question.was_published_recently()はFalseを返さなくてはならない
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)

    ## pub_dateが過去になっているときに「最近作られた」と誤判断されないか？
    def test_was_published_recently_with_old_question(self):
        # あるQuestionオブジェクトold_questionのpub_dateが過去（ここでは1日（24時間0分）1秒前）になっているとき、
        # old_question.was_published_recently()はFalseを返さなくてはならない
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)

        self.assertIs(old_question.was_published_recently(), False)

    ## pub_dateが最近になっているときに「最近作られた」と判断されるか？
    def test_was_published_recently_with_recent_question(self):
        # あるQuestionオブジェクトrecent_questionのpub_dateが直近1日以内（ここでは23時間59分59秒前）になっているとき、
        # recent_question.was_published_recently()はTrueを返さなくてはならない
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)

        self.assertIs(recent_question.was_published_recently(), True)
