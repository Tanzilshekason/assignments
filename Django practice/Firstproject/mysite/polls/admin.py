from django.contrib import admin
from .models import Article

admin.site.site_header = 'POLLS ADMIN'
admin.site.site_title = 'POLLS ADMIN PORTAL'
admin.site.index_title = 'WELCOME TO POLLS ADMIN PORTAL'

admin.site.register(Article)


class ArticleAdminSite(admin.ModelAdmin):
    model = Article
    fields = ['title', 'slug', 'body', 'date']
    list_display = ('title', 'slug', 'body', 'date')
    actions = ['description']

def description(self, request, queryset):
    queryset.update(is_good=False)


    admin.site.register(Article.ArticleAdminSite)
