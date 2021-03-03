from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.title


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    link = models.CharField(max_length=300, verbose_name='Айди с youtube')
    text = models.TextField(verbose_name='Описание')
    type = models.BooleanField(default=True, verbose_name='В тренде')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=2000)
    comment = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.comment

