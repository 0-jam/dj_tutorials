# Django tutorials

- [Django][django]（当時2.1）の[チュートリアル][djtut]をなぞるだけ
- 一部Railsで同じことをするためのコマンドなどをコメントに書いている
- Python 3.8.2,  Django 3.0.4

---

1. [Memo](#memo)

---

## Memo

- Railsでいう`latest_questions.pluck(question_text)`

```python
latest_questions = Question.objects.order_by("-pub_date")[:5]
output = ', '.join([q.question_text for q in latest_questions])
```

- [ユニットテストで使うメソッド集][pyutest]
    - `assertFalse()`というメソッドもあるが、pollsアプリケーションのテストは`assertIs()`で値を **`False`そのものと比較** している
    - [Python3でFalse扱いされる数値][pyfalse]
        - `assertFalse()`はこれらと一致しているかを判定するらしい
        - `None`, `False`, 各種カラの値（ゼロや空文字列など）
- チュートリアル6で扱う静的ファイルは、追加したあとサーバーを再起動する必要がある？
    - チュートリアル中では _リロードすれば（中略）変わったはず_ とあるが、単にリロードするとstyle.cssをロードするときに404エラー

[django]: http://djangoproject.jp/
[djtut]: https://docs.djangoproject.com/en/3.0/
[pyutest]: https://docs.python.jp/3/library/unittest.html
[pyfalse]: https://docs.python.jp/3/library/stdtypes.html#truth-value-testing
