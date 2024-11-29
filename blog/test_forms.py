from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Tests for the CommentForm.
    """

    def test_form_is_valid(self):
        """
        Test that the form is valid when provided with valid data.
        """
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        """
        Test that the form is invalid when the body field is empty.
        """
        comment_form = CommentForm({'body': ''})
        self.assertFalse(
            comment_form.is_valid(),
            msg="The form should not be valid with an empty body."
        )
