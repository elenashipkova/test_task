from http import HTTPStatus
from urllib import response

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from articles.models import Article, Author

User = get_user_model()


class ArticleURLTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='loginuser')
        cls.guest = User.objects.create_user(username='guestuser')
    
    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(ArticleURLTests.user)
        self.author = Author.objects.create(
            name='Test', birth_date='1955-01-21'
        )
        self.article = Article.objects.create(
            title='Test title', text='Test text'
        )
        self.article.authors.add(self.author)

    def test_url_pages_exists_at_desired_location(self):
        article_id = self.article.id
        url_pages = (
            ('/', self.authorized_client),
            (f'/{article_id}/', self.authorized_client),
            (f'/{article_id}/edit/', self.authorized_client),
            ('/new/', self.authorized_client),
            ('/authors/', self.client),
        )
        for page, page_client in url_pages:
            with self.subTest(page=page):
                response = page_client.get(page)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_pages_use_correct_names(self):
        article_id = self.article.id
        url_pages_names = (
            ('/', 'articles', None),
            (f'/{article_id}/', 'article_view', (article_id,)),
            (f'/{article_id}/edit/', 'article_edit', (article_id,)),
            ('/new/', 'new_article', None),
            ('/authors/', 'authors', None),
        )
        for page, page_name, arg in url_pages_names:
            with self.subTest(page=page):
                self.assertEqual(page, reverse(page_name, args=arg))

    def test_url_pages_redirect_users_to_login_page(self):
        article_id = self.article.id
        login_page = reverse('login')
        index_page = reverse('articles')
        new_article_page = reverse('new_article')
        article_page = reverse('article_view', args=(article_id,))
        article_edit_page = reverse('article_edit', args=(article_id,))
        redirect_pages_names = (
            ('/', self.client, f'{login_page}?next={index_page}'),
            (f'/{article_id}/', self.client, f'{login_page}?next={article_page}'),
            (f'/{article_id}/edit/', self.client, f'{login_page}?next={article_edit_page}'),
            ('/new/', self.client, f'{login_page}?next={new_article_page}')
        )
        for page, page_client, redirect_page in redirect_pages_names:
            with self.subTest(page=page):
                response = page_client.get(page)
                self.assertRedirects(response, redirect_page)