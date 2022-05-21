from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArticleForm
from .models import Article, Author


@login_required
def articles(request):
    articles = Article.objects.prefetch_related('authors')
    return render(request, 'articles.html', {'articles': articles})


@login_required
def new_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save()
        article.save()
        return redirect('articles')
    return render(request, 'new.html', {'form': form, 'edit': False})


@login_required
def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles')
    return render(
        request, 'new.html', {'form': form, 'article': article, 'edit': True}
    )


def authors(request):
    authors = Author.objects.prefetch_related('articles').all()
    return render(request, 'authors.html', {'authors': authors})

@login_required
def article_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {'article': article})
