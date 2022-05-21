from django.urls import path

from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:article_id>', views.article_view, name='article_view'),
    path('<int:article_id>/edit', views.article_edit, name='article_edit'),
    path('new/', views.new_article, name='new_article'),
    path('authors/', views.authors, name='authors'),
]