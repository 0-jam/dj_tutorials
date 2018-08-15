# $ python manage.py test polls でテストを実行できる

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

import datetime

from .models import Question

# Create your tests here.

## モデルのテストクラス
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

    ## pub_dateが最近になっているときに「最近作られた」と正しく判断されるか？
    def test_was_published_recently_with_recent_question(self):
        # あるQuestionオブジェクトrecent_questionのpub_dateが直近1日以内（ここでは23時間59分59秒前）になっているとき、
        # recent_question.was_published_recently()はTrueを返さなくてはならない
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)

        self.assertIs(recent_question.was_published_recently(), True)

## Questionオブジェクトを作る
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)

    return Question.objects.create(question_text=question_text, pub_date=time)

### ビューのテストクラス
## index
class QuestionIndexViewTests(TestCase):
    # 質問が存在しないときの表示、各変数の状態
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            []
        )

    # 過去の質問のみの表示、各変数の状態
    def test_past_question(self):
        create_question(question_text="Past question.", days=-30)

        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Past question.>']
        )

    # 未来の質問のみの表示、各変数の状態
    def test_future_question(self):
        create_question(question_text="Future question.", days=30)

        response = self.client.get(reverse('polls:index'))

        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            []
        )

    # 過去と未来と両方に質問があるときの表示、各変数の状態
    def test_future_and_past_questions(self):
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)

        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Past question.>']
        )

    # 過去の質問が2つあるときの表示、各変数の状態
    def test_two_past_questions(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)

        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

## detail
class QuestionDetailViewTests(TestCase):
    # 未来の質問が表示されないことを確認
    def test_future_question(self):
        future_question = create_question(question_text="Future Question.", days=5)

        response = self.client.get(reverse('polls:detail', args=(future_question.id,)))

        self.assertEqual(response.status_code, 404)

    # 未来の質問が表示されないことを確認
    def test_past_question(self):
        past_question = create_question(question_text="Past Question.", days=-5)

        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))

        self.assertContains(response, past_question.question_text)
