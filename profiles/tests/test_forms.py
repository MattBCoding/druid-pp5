from django.test import TestCase
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from profiles.forms import AddressForm, DeleteUserForm, EditUserForm
from profiles.models import Address


class TestAddressForm(TestCase):
    '''
    Unit test for Address Form
    '''

    def test_address_street_address_one_is_required(self):
        form = AddressForm(({'street_address_1': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('street_address_1', form.errors.keys())
        self.assertEqual(form.errors['street_address_1'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        form = AddressForm(({'town_or_city': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0], 'This field is required.')

    def test_country_code_is_required(self):
        form = AddressForm(({'country': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')

    def test_user_field_excluded(self):
        form = AddressForm()
        self.assertEqual(form.Meta.exclude, ('user',))


class TestDeleteUserForm(TestCase):
    '''
    Unit tests for DeleteUserForm
    '''

    def test_email_field_is_required(self):
        form = DeleteUserForm(({'email': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')


class TestEditUserForm(TestCase):
    '''
    Unit tests for EditUserForm
    '''
    def test_first_name_field_required(self):
        form = EditUserForm(({'first_name': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')

    def test_last_name_field_required(self):
        form = EditUserForm(({'last_name': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0], 'This field is required.')
