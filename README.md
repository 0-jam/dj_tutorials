# Django test

- [Django][django]2.1の[チュートリアル][djtut]をなぞるだけ
- 一部Railsで同じことをするためのコマンドなどをコメントに書いている

---

1. [Progress](#progress)
1. [Memo](#memo)

---

## Progress

- [x] [Tutorial 01](https://docs.djangoproject.com/ja/2.1/intro/tutorial01/)
- [x] [Tutorial 02](https://docs.djangoproject.com/ja/2.1/intro/tutorial02/)
- [x] [Tutorial 03](https://docs.djangoproject.com/ja/2.1/intro/tutorial03/)
- [ ] [Tutorial 04](https://docs.djangoproject.com/ja/2.1/intro/tutorial04/)
- [ ] [Tutorial 05](https://docs.djangoproject.com/ja/2.1/intro/tutorial05/)
- [ ] [Tutorial 06](https://docs.djangoproject.com/ja/2.1/intro/tutorial06/)
- [ ] [Tutorial 07](https://docs.djangoproject.com/ja/2.1/intro/tutorial07/)

## Memo

- Railsでいう`latest_question_list.pluck(question_text)`
    - pluck的なのないのかな？

```python
latest_question_list = Question.objects.order_by("-pub_date")[:5]
output = ', '.join([q.question_text for q in latest_question_list])
```

[django]: http://djangoproject.jp/
[djtut]: https://docs.djangoproject.com/ja/2.1/intro/
