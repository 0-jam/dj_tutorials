from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

## pollsアプリケーション（Railsでいうコントローラー）の各アクション
def index(request):
    # 最新5件の質問
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # コントローラーからビューに渡したい変数
    context = {
        'latest_question_list': latest_question_list,
    }

    # 以下と同じだが、長いので使わないほうがよさそう…
    # return HttpResponse(loader.get_template('polls/index.html').render(context, request))
    # 無理やりRailsに例えると`render('index', context: context)`かな？
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # 指定された条件に合致するレコードがQuestionモデルにないときに例外
    # objects.filterに相当する`get_list_or_404`もある
    question = get_object_or_404(Question, pk=question_id)
    # 以下と同じ
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

## ユーザーのpostを受け取る
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

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
