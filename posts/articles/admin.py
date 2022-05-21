from django.contrib import admin

from .models import Article, Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
    list_filter = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date')
    search_fields = ('pub_date',)
    list_filter = ('title',)
    filter_horizontal = ('authors',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
