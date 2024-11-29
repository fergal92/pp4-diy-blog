from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Post model.
    """
    list_display = ('title', 'slug', 'status', 'created_on', 'image_thumbnail')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    def make_published(self, request, queryset):
        """
        Custom admin action to mark selected posts as published.
        """
        queryset.update(status='published')
    make_published.short_description = "Mark selected posts as Published"

    def image_thumbnail(self, obj):
        """
        Display a thumbnail for the featured image in the admin list.
        """
        if obj.featured_image:
            return format_html(
                '<img src="{}" width="10" height="10" alt="Thumbnail" />',
                obj.featured_image.url
            )
        return "No Image"


# Register Comment model.
admin.site.register(Comment)
