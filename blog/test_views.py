from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post
from unittest.mock import patch

class TestBlogViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post.objects.create(
            title="Blog title",
            author=self.user,
            slug="blog-title",
            excerpt="Blog excerpt",
            content="Blog content",
            status=1
        )

    @patch('cloudinary.uploader.upload')
    @patch('cloudinary.CloudinaryImage')
    def test_render_post_detail_page_with_comment_form(
        self, mock_cloudinary_image, mock_upload
    ):
        mock_cloudinary_image.return_value.url = "http://example.com/test.jpg"
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    @patch('cloudinary.uploader.upload')
    @patch('cloudinary.CloudinaryImage')
    def test_successful_comment_submission(
        self, mock_cloudinary_image, mock_upload
    ):
        mock_cloudinary_image.return_value.url = "http://example.com/test.jpg"
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'body': 'This is a test comment.'}
        response = self.client.post(
            reverse('post_detail', args=['blog-title']), post_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )