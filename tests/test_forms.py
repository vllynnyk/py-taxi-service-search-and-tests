from django.test import TestCase

from taxi.forms import DriverCreationForm


class FormsTests(TestCase):
    def test_driver_creation_form(self):
        form_data = {
            "username": "like_god",
            "password1": "1234pass",
            "password2": "1234pass",
            "first_name": "testfirst",
            "last_name": "testlast",
            "license_number": "ASD12345",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
