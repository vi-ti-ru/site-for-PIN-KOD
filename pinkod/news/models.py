from django.db import models

class articles(models.Model):
    title = models.CharField('название',max_length=50, default='-')
    anons = models.CharField('анонс', max_length=250, default='-')
    full_text = models.TextField('Статья')
    date = models.DateTimeField("Дата публикации")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"