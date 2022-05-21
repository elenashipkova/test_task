from django.forms import CheckboxSelectMultiple, ModelForm, ModelMultipleChoiceField

from .models import Article, Author


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'authors', 'text')
        labels = {
            'title': 'Заголовок статьи',
            'authors': 'Автор(ы)',
            'text': 'Текст'
        }
        help_texts = {
            'title': 'Заголовок должен отражать содержание статьи',
            'authors': 'Укажите как минимум одного автора',
            'text': 'Введите текст статьи',
        }
        authors = ModelMultipleChoiceField(
            queryset=Author.objects.all(),
            widget=CheckboxSelectMultiple()
        )

