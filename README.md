На данный момент реализован базовый функционал.
Горячие клавиши сохранения и открытия файла: Ctrl-S и Ctrl-O.

Все имеющиеся поля, кроме смены шрифта на данный момент рабочие.

Правое нижнее удаляет строку по индексу.

Поле справа сверху делает поиск подстроки.

Поля справа посередине отвечают за замену подстроки на другую.

Так как не все функции библиотеки customtkinter прописаны разработчиком, то необходимо добавить в CTkTextbox следующие методы:

```
    def delete(self, *args, **kwargs):
        return self.textbox.delete(*args, **kwargs)

    def get(self, index1, index2):
        return self.textbox.get(index1, index2)

    def search(self, *args, **kwargs):
        return self.textbox.search(*args, **kwargs)
 ```
