from django.test import TestCase
from.models import Posts
from django.utils import timezone

class PostsModelTest(TestCase):

    def test_string_representation(self):
        entry = Posts(post_title="My entry title")
        self.assertEqual(str(entry), entry.post_title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Posts._meta.verbose_name_plural), "posts")

class PostsViewTests(TestCase):
    def setUp(self):
        model_posts = Posts.objects.create(user='user', post_title='title', post_text='text', post_url='url',
                            post_date=timezone.now())

    def test_show_posts(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_show_posts_top(self):
        response = self.client.get('/top/')
        self.assertEqual(response.status_code, 200)

    def test_show_post_comments(self):
        model_posts = Posts(user='user', post_title='title', post_text='text', post_url='url',
                            post_date=timezone.now())
        model_posts.save()
        response = self.client.get('/get/1')
        self.assertEqual(response.status_code, 200)
