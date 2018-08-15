# Django test

- [Django][django]2.1の[チュートリアル][djtut]をなぞるだけ
- 一部Railsで同じことをするためのコマンドなどをコメントに書いている
- Python 3.7.0,  Django 2.1

---

1. [Progress](#progress)
1. [Memo](#memo)

---

## Progress

- [x] [Tutorial 01](https://docs.djangoproject.com/ja/2.1/intro/tutorial01/)
- [x] [Tutorial 02](https://docs.djangoproject.com/ja/2.1/intro/tutorial02/)
- [x] [Tutorial 03](https://docs.djangoproject.com/ja/2.1/intro/tutorial03/)
- [x] [Tutorial 04](https://docs.djangoproject.com/ja/2.1/intro/tutorial04/)
- [x] [Tutorial 05](https://docs.djangoproject.com/ja/2.1/intro/tutorial05/)
    - [ ] ResultsViewのテストも作ってみよう
    - [ ] 選択肢がない質問も表示しないようにしよう
    - [テスト参考][djtesting]
- [ ] [Tutorial 06](https://docs.djangoproject.com/ja/2.1/intro/tutorial06/)
- [ ] [Tutorial 07](https://docs.djangoproject.com/ja/2.1/intro/tutorial07/)

## Memo

- Railsでいう`latest_questions.pluck(question_text)`
    - pluck的なのないのかな？

```python
latest_questions = Question.objects.order_by("-pub_date")[:5]
output = ', '.join([q.question_text for q in latest_questions])
```

- [ユニットテストで使うメソッド集][pyutest]
    - `assertFalse()`というメソッドもあるが、pollsアプリケーションのテストは`assertIs()`で値を **`False`そのものと比較** している
    - [Python3でFalse扱いされる数値][pyfalse]
        - `assertFalse()`はこれらと一致しているかを判定するらしい
        - `None`, `False`, 各種カラの値（ゼロや空文字列など）

[django]: http://djangoproject.jp/
[djtut]: https://docs.djangoproject.com/ja/2.1/intro/
[pyutest]: https://docs.python.jp/3/library/unittest.html
[pyfalse]: https://docs.python.jp/3/library/stdtypes.html#truth-value-testing
[djtesting]: https://docs.djangoproject.com/ja/2.1/topics/testing/
