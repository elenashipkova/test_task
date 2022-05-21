from django.test import TestCase

from articles.models import Article, Author


class ModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = Author.objects.create(
            name='Test1', birth_date='1956-01-21'
        )
        cls.article = Article.objects.create(
            title='Test title 1', text='Test text 1'
        )
        cls.article.authors.add(cls.author)

    def test_article_verboses_names_is_correct(self):
        article = ModelTest.article
        field_verboses = {
            'title': 'Заголовок',
            'text': 'Текст статьи',
            'pub_date': 'Дата публикации',
            'authors': 'Авторы',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    article._meta.get_field(field).verbose_name, expected_value
                )
    
    def test_author_verboses_names_is_correct(self):
        author = ModelTest.author
        field_verboses = {
            'name': 'Фамилия Имя Отчество полностью',
            'birth_date': 'Дата рождения',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    author._meta.get_field(field).verbose_name, expected_value
                )
    
    def test_str_method_of_models_is_correct(self):
        article = ModelTest.article
        author = ModelTest.author
        objects_str_method = {
            article: f"{article.title} ({author.name})",
            author: f'{author.name}, {author.birth_date}'
        }
        for objects, expected_str in objects_str_method.items():
            with self.subTest(object=object):
                self.assertEqual(str(objects), expected_str)
                