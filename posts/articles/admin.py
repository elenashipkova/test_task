from django.contrib import admin

from .models import Article, Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name__startswith',)
    list_filter = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date')
    search_fields = ('title__icontains',)
    list_filter = ('pub_date', 'authors__name')
    filter_horizontal = ('authors',)
    empty_value_display = '-пусто-'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
