from django.test import TestCase
from blog.forms import BlogPostForm
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile

from druid.settings import MEDIA_ROOT


class TestBlogPostForm(TestCase):
    '''
    Unit tests for the BlogPostForm
    '''

    def test_title_is_required(self):
        form = BlogPostForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_category_is_required(self):
        form = BlogPostForm(({'category': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_image_url_field_requires_url(self):
        form = BlogPostForm(({'image_url': 'hi this is not a url'}))
        self.assertFalse(form.is_valid())
        self.assertIn('image_url', form.errors.keys())
        self.assertEqual(form.errors['image_url'][0], 'Enter a valid URL.')

    def test_image_url_field_accepts_url(self):
        # complete image url field in form
        form = BlogPostForm((
            {'image_url': 'https://en.wikipedia.org/wiki/File:Test_image.jpg'}
            ))
        # form will still be invalid as other fields not complete
        self.assertFalse(form.is_valid())
        # image url field not in error list - confirms its correctly filled in.
        self.assertNotIn('image_url', form.errors.keys())

    def test_image_field_accepts_image_file(self):
        image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        form = BlogPostForm(({'image': image}))
        self.assertFalse(form.is_valid())
        self.assertNotIn('image', form.errors.keys())

    def test_content_is_required(self):
        form = BlogPostForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')
