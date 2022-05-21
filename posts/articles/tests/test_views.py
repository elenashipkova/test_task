from urllib import response
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from articles.forms import ArticleForm
from articles.models import Article, Author

User = get_user_model()


class ArticlePagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='user')
        cls.author1 = Author.objects.create(
            name='Test2', birth_date='1957-01-21'
        )
        cls.author2 = Author.objects.create(
            name='Test3', birth_date='1958-01-21'
        )
        cls.article = Article.objects.create(
            title='Test title 2', text='Test text 2'
        )
        cls.article.authors.add(cls.author1, cls.author2)
    
    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(ArticlePagesTests.user)
    
    def test_pages_use_correct_templates(self):
        article_id = ArticlePagesTests.article.id
        templates_pages_names = (
            ('articles.html', 'articles', None),
            ('article.html', 'article_view', (article_id,)),
            ('new.html', 'article_edit', (article_id,)),
            ('new.html', 'new_article', None),
            ('authors.html', 'authors', None)
        )
        for template, reverse_name, arg in templates_pages_names:
            with self.subTest(template=template):
                response = self.authorized_client.get(
                    reverse(reverse_name, args=arg)
                )
                self.assertTemplateUsed(response, template)
    
    def test_articles_page_shows_correct_context(self):
        response = self.authorized_client.get(reverse('articles'))
        self.assertIn('articles', response.context)

    def test_new_article_page_shows_correct_context(self):
        response = self.authorized_client.get(reverse('new_article'))
        self.assertIn('form', response.context)
        self.assertIn('edit', response.context)
        self.assertIsInstance(response.context['form'], ArticleForm)
        self.assertIs(response.context['edit'], False)

    def test_edit_article_page_shows_correct_context(self):
        article_id = ArticlePagesTests.article.id
        response = self.authorized_client.get(
            reverse('article_edit', args=(article_id,))
        )
        self.assertIn('form', response.context)
        self.assertIn('edit', response.context)
        self.assertIsInstance(response.context['form'], ArticleForm)
        self.assertIs(response.context['edit'], True)

    def test_article_page_shows_correct_context(self):
        article_id = ArticlePagesTests.article.id
        response = self.authorized_client.get(
            reverse('article_view', args=(article_id,))
        )
        self.assertIn('article', response.context)
    
    def test_authors_page_shows_correct_context(self):
        response = self.client.get(reverse('authors'))
        self.assertIn('authors', response.context)
    