from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Post


class PostsModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text="This is a test!")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'This is a test!')


class HomePageViewTest(TestCase):
    test_string = "This is another Test!"

    def setUp(self):
        Post.objects.create(text=self.test_string)

    def test_view_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
