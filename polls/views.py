from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# 汎用ビュー使用前は以下も必要
# from django.http import HttpResponse, Http404

from .models import Question, Choice

# Create your views here.


# 汎用ビュー使用
# defじゃないことに注意
class IndexView(generic.ListView):
    # コンテキスト変数を指定
    # default: 'polls/question_list.html'(<app_name>/<model_name>_list.html)
    template_name = 'polls/index.html'
    # default: question_list
    context_object_name = 'latest_questions'

    def get_queryset(self):
        # 最新5件のpub_dateが未来の日時でない質問を返す
        # __lte: less than or equal to
        # pub_date <= timezone.now() のようには書けない
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # ここで表示したいモデルの名前を指定
    model = Question
    # default: 'polls/question_detail.html'(<app_name>/<model_name>_detail.html)
    template_name = 'polls/detail.html'

    def get_queryset(self):
        # 未来の質問を除外する
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    # もちろん同じ汎用ビューに違うテンプレートを指定できる
    template_name = 'polls/results.html'


# ユーザーのpostを受け取る
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        # request.POST['choice']：Railsのparams[:choice]に相当
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 投票対象が選択されていない場合、投票フォームに戻る
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': "You didn't select a choice."
            }
        )
    else:
        # 投票数を更新
        selected_choice.votes += 1
        selected_choice.save()

        # 戻るボタンを押したときに二重送信されるのを防ぐため、
        # 送信されたデータを正しく処理できた場合のみリダイレクトする
        # ハードコーディング防止のためにreverse()を使っている
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# 以下汎用ビュー使用前
# pollsアプリケーション（Railsでいうコントローラー）の各アクション
# def index(request):
#     # 最新5件の質問
#     latest_questions = Question.objects.order_by("-pub_date")[:5]

#     # コントローラーからビューに渡したい変数
#     context = {
#         'latest_questions': latest_questions,
#     }

#     # 以下と同じだが、長いので使わないほうがよさそう…
#     # return HttpResponse(loader.get_template('polls/index.html').render(context, request))
#     # 無理やりRailsに例えると`render('index', context: context)`かな？
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     # 指定された条件に合致するレコードがQuestionモデルにないときに例外
#     # objects.filterに相当する`get_list_or_404`もある
#     question = get_object_or_404(Question, pk=question_id)
#     # 以下と同じ
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist.")
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
