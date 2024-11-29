from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from unittest.mock import patch
from .forms import CommentForm
from .models import Post


class TestBlogViews(TestCase):
    """
    Tests for blog views including rendering post details
    and comment submission.
    """

    def setUp(self):
        """
        Set up test data including a user and a blog post.
        """
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
        """
        Test rendering the post detail page with the comment form.
        """
        mock_cloudinary_image.return_value.url = (
            "http://example.com/test.jpg"
        )
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        self.assertEqual(
            response.status_code,
            200,
            msg="Page did not load successfully."
        )
        self.assertIn(
            b"Blog title",
            response.content,
            msg="Title not found in page content."
        )
        self.assertIn(
            b"Blog content",
            response.content,
            msg="Content not found in page content."
        )
        self.assertIsInstance(
            response.context['comment_form'],
            CommentForm,
            msg="Comment form is not included in the context."
        )

    @patch('cloudinary.uploader.upload')
    @patch('cloudinary.CloudinaryImage')
    def test_successful_comment_submission(
        self, mock_cloudinary_image, mock_upload
    ):
        """
        Test submitting a comment successfully for a post.
        """
        mock_cloudinary_image.return_value.url = (
            "http://example.com/test.jpg"
        )
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'body': 'This is a test comment.'}
        response = self.client.post(
            reverse('post_detail', args=['blog-title']),
            post_data
        )
        self.assertEqual(
            response.status_code,
            200,
            msg="Comment submission did not return expected status code."
        )
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content,
            msg=(
                "Success message for comment submission not found "
                "in page content."
            )
        )
