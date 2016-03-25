from django.contrib import admin
from terryspace.blog.models import Author,Classification,Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','classification','author',)
    search_field = ('title',)
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','email',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Classification)
admin.site.register(Article,ArticleAdmin)

