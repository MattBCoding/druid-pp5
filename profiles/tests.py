from django.test import TestCase
from django.contrib.auth import get_user_model


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

    def testProfilePage(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='profiles/profile.html')
    
    def testLoggedOutProfilePage(self):
        # test to see if the user is logged out
        # that when you attempt to access the profile page
        # the user is redirected
        self.client.logout()
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 302)
