from .models import Comment, Post
from django.core.exceptions import ValidationError
from django import forms

def validate_file_size(file):
    max_size = 10 * 1024 * 1024  # 10MB
    if file.size > max_size:
        raise ValidationError(f"File size too large. Maximum size is {max_size // (1024 * 1024)}MB.")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'featured_image']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['featured_image'].validators.append(validate_file_size)