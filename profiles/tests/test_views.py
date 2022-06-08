from django.test import TestCase
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from profiles.forms import AddressForm
from profiles.models import Address


# Create your tests here.
class TestViews(TestCase):
    '''Unit tests for the profiles app views'''

    def setUp(self):
        '''
        set up a user and log them in to test
        views that require the user to be logged in
        '''
        username = 'testuser'
        email = 'test@test.com'
        password = 'testpassword1234!'
        first_name = 'test'
        last_name = 'surname'
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username=username,
                                                    first_name=first_name,
                                                    last_name=last_name,
                                                    email=email, 
                                                    password=password)
        log_in = self.client.login(username=username,
                                    email=email,
                                    password=password)

        # confirm that the user is logged in
        self.assertTrue(log_in)

    def test_profile_page(self):
        '''
        test the profile page url 
        '''
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
    
    def test_profile_page_template(self):
        '''
        test the correct template is used
        '''
        response = self.client.get('/profiles/')
        self.assertTemplateUsed(response, template_name='profiles/profile.html')

    def test_logged_out_profile_page(self):
        '''
        test to see if the user is logged out
        that when you attempt to access the profile page
        the user is redirected
        '''
        self.client.logout()
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 302)
    
    def test_add_address_page(self):
        '''
        Test to see if the user is logged in
        that they can access the add address page
        '''
        response = self.client.get('/profiles/add_address/')
        # confirm url returns page
        self.assertEqual(response.status_code, 200)
    
    def test_add_address_page_template(self):
        '''
        Test to confirm template used to add address
        '''
        response = self.client.get('/profiles/add_address/')
        self.assertTemplateUsed(response, template_name='profiles/address_form.html')

    def test_logged_out_add_address_page(self):
        '''
        Test to check user is redirected if not logged in
        and they try to access the add address page
        '''
        self.client.logout()
        response = self.client.get('/profiles/add_address/')
        self.assertEqual(response.status_code, 302)

    def test_logged_in_add_address(self):
        '''
        This test checks that a logged in user
        can add an address to their profile
        '''
        request = HttpRequest()
        request.POST = {
            'street_address_1': 'test address line 1',
            'street_address_2': 'test address line 2',
            'town_or_city': 'testtown',
            'county': 'testcounty',
            'postcode': 'testpostcode',
            'country': 'IE',
            'phone_number': '012345678910',
            'default': 'false'
        }
        # form = AddressForm(request.POST)
        # form.save(commit=False)
        # form.user = self.user
        # form.save()
        response = self.client.post('/profiles/add_address/', request.POST)
        # confirm address object was added
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
    
    def test_address_default_override(self):
        '''
        This tests that when a user adds a new address
        that is tagged as default, the default tag is removed from
        the previous default address.
        '''
        address_data_one = {
            'street_address_1': 'test address line 1 set one',
            'street_address_2': 'test address line 2 set one',
            'town_or_city': 'testtown',
            'county': 'testcounty',
            'postcode': 'testpostcode',
            'country': 'IE',
            'phone_number': '012345678910',
            'default': 'True'
        }

        address_data_two = {
            'street_address_1': 'test address line 1 set two',
            'street_address_2': 'test address line 2 set two',
            'town_or_city': 'testtown',
            'county': 'testcounty',
            'postcode': 'testpostcode',
            'country': 'IE',
            'phone_number': '012345678910',
            'default': 'True'
        }
        # post address data one to url
        self.client.post('/profiles/add_address/', address_data_one)
        # confirm one address object exists
        self.assertEqual(Address.objects.count(), 1)
        # confirm one address object exists with default == True
        self.assertEqual(Address.objects.filter(default__exact=True).count(), 1)
        # post address data two to url
        self.client.post('/profiles/add_address/', address_data_two)
        # confirm two addresses now exist
        self.assertEqual(Address.objects.count(), 2)
        # confirm only one address object has default tag
        self.assertEqual(Address.objects.filter(default__exact=True).count(), 1)

    def test_edit_address_page(self):
        '''
        test to see if logged in user can access the add address page
        '''
        address_data_one = {
            'street_address_1': 'test address line 1 set one',
            'street_address_2': 'test address line 2 set one',
            'town_or_city': 'testtown',
            'county': 'testcounty',
            'postcode': 'testpostcode',
            'country': 'IE',
            'phone_number': '012345678910',
            'default': 'True'
        }
        self.client.post('/profiles/add_address/', address_data_one)
        self.assertEqual(Address.objects.count(), 1)
        address = get_object_or_404(Address, user=self.user)
        id = str(address.id)
        response = self.client.get(f'/profiles/edit_address/{id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/address_form.html')
        self.assertTrue(response.context['address'].pk == address.id)

    def test_logged_out_edit_address_page(self):
        '''
        test to see if a logged out user is redirected when trying
        to access the edit address page
        '''
        address_data_one = {
            'street_address_1': 'test address line 1 set one',
            'street_address_2': 'test address line 2 set one',
            'town_or_city': 'testtown',
            'county': 'testcounty',
            'postcode': 'testpostcode',
            'country': 'IE',
            'phone_number': '012345678910',
            'default': 'True'
        }
        self.client.post('/profiles/add_address/', address_data_one)
        self.assertEqual(Address.objects.count(), 1)
        address = get_object_or_404(Address, user=self.user)
        id = str(address.id)
        self.client.logout()
        response = self.client.get(f'/profiles/edit_address/{id}/')
        self.assertEqual(response.status_code, 302)

    def test_delete_address_view(self):
        '''
        Test deleting address
        '''
        address_data_one = {
            'street_address_1': 'test address line 1 set one',
            'street_address_2': 'test address line 2 set one',
            'town_or_city': 'testtown',
            'county': 'testcounty',
            'postcode': 'testpostcode',
            'country': 'IE',
            'phone_number': '012345678910',
            'default': 'True'
        }
        self.client.post('/profiles/add_address/', address_data_one)
        self.assertEqual(Address.objects.count(), 1)
        address = get_object_or_404(Address, user=self.user)
        id = str(address.id)
        response = self.client.post(f'/profiles/delete_address/{id}/')
        self.assertTrue(response.status_code, 200)
        self.assertEqual(Address.objects.count(), 0)


