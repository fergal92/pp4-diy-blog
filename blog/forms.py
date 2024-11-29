from django import forms
from django.core.exceptions import ValidationError
from .models import Comment, Post


def validate_file_size(file):
    """
    Custom validator to ensure file size does not exceed 10MB.
    """
    max_size = 10 * 1024 * 1024  # 10MB
    if file.size > max_size:
        readable_max_size = max_size // (1024 * 1024)
        raise ValidationError(
            f"File size too large. "
            f"Maximum size is {readable_max_size}MB."
        )


class CommentForm(forms.ModelForm):
    """
    Form for creating and managing comments.
    """
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    Form for creating and managing posts, including a custom validator
    for the featured image size.
    """
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'featured_image']

    def __init__(self, *args, **kwargs):
        """
        Add a custom file size validator for the featured_image field.
        """
        super().__init__(*args, **kwargs)
        self.fields['featured_image'].validators.append(validate_file_size)
