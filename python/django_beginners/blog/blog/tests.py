from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


# Create your tests here.
class BlogsTest(TestCase):
    Testing_Title = 'This is a good testing title'
    Testing_Body = 'This is the body for that test!'

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='loganstartoni+testingemail@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title=self.Testing_Title,
            body=self.Testing_Body,
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title=self.Testing_Title)
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', self.Testing_Title)
        self.assertEqual(f'{self.post.body}', self.Testing_Body)
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.Testing_Body)
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/1000000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.Testing_Title)
        self.assertTemplateUsed(response, 'post_details.html')
