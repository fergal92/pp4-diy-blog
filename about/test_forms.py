from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):
    """Test suite for the CollaborateForm."""

    def test_form_is_valid(self):
        """Test for all fields when the form is valid."""
        form_data = {
            'name': 'Matt',
            'email': 'test@test.com',
            'message': 'Hello!'
        }
        form = CollaborateForm(form_data)
        print("Form errors:", form.errors)
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test for the 'name' field when it is empty."""
        form_data = {
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        }
        form = CollaborateForm(form_data)
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field when it is empty."""
        form_data = {
            'name': 'Matt',
            'email': '',
            'message': 'Hello!'
        }
        form = CollaborateForm(form_data)
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field when it is empty."""
        form_data = {
            'name': 'Matt',
            'email': 'test@test.com',
            'message': ''
        }
        form = CollaborateForm(form_data)
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )
