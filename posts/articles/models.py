from django.db import models


class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField('Фамилия Имя Отчество полностью', max_length=100)
    birth_date = models.DateField('Дата рождения')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}, {self.birth_date}'


class Article(models.Model):
    """
    Model representing an article.
    """
    title = models.CharField('Заголовок', max_length=256)
    authors = models.ManyToManyField(Author,
                                     related_name='articles',
                                     verbose_name='Авторы')
    text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-pub_date',)
    
    def __str__(self):
        return f"{self.title} ({', '.join(author.name for author in self.authors.all())})"
