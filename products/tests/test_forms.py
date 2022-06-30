from django.test import TestCase
from products.forms import ProductForm, ReviewForm, ResponseForm
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile


class TestReviewForm(TestCase):
    '''
    Unit tests for the ReviewForm
    '''

    def test_rating_is_required(self):
        form = ReviewForm(({'rating': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')


class TestResponseForm(TestCase):
    '''
    Unit tests for the ResponseForm
    '''

    def test_response_field_is_required(self):
        form = ResponseForm(({'response': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('response', form.errors.keys())
        self.assertEqual(form.errors['response'][0], 'This field is required.')


class TestProductForm(TestCase):
    '''
    Unit tests for the ProductForm
    '''

    def test_description_is_required(self):
        form = ProductForm(({'description': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_price_is_required(self):
        form = ProductForm(({'price': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_image_field_accepts_image_file(self):
        image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        form = ProductForm(({'image': image}))
        self.assertFalse(form.is_valid())
        self.assertNotIn('image', form.errors.keys())
