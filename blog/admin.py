from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on', 'image_thumbnail')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    def make_published(self, request, queryset):
        queryset.update(status='published')
    make_published.short_description = "Mark selected posts as Published"
    
    def image_thumbnail(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" width="10" height="10" />', obj.featured_image.url)
        return "No Image"
    
# Register your models here.
admin.site.register(Comment)
