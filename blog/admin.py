from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)
    date_hierarchy = ('publish')
    ordering = ('status', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created', 'publish', 'author')
    list_display = ('title', 'slug', 'author', 'publish', 'status')
