from django.test import TestCase
from.models import Posts, Likes_Post, Comments
from django.utils import timezone
from django.contrib.auth.forms import User

class PostsModelTest(TestCase):
    """тестирование методов модели"""
    def test_string_representation(self):
        entry = Posts(post_title="My entry title")
        self.assertEqual(str(entry), entry.post_title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Posts._meta.verbose_name_plural), "posts")

class LikesPostModelTest(TestCase):
    """тестирование методов модели"""
    def test_verbose_name_plural(self):
        self.assertEqual(str(Likes_Post._meta.verbose_name_plural), "likes")

class CommentsModelTest(TestCase):
    """тестирование методов модели"""
    def test_verbose_name_plural(self):
        self.assertEqual(str(Comments._meta.verbose_name_plural), "comments")

class PostsViewTests(TestCase):

    def setUp(self):
        User.objects.create_user(username='username', password='password')
        Posts.objects.create(user='user', post_title='title', post_text='text', post_url='url',
                             post_date=timezone.now())

    def test_show_posts(self):
        """тестирование метода вывод постов"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_show_posts_top(self):
        """тестирование метода вывода постов в топе"""
        response = self.client.get('/user/top/')
        self.assertEqual(response.status_code, 200)

    def test_show_post_comments(self):
        """тестирование метода вывода поста с коментариями"""
        response = self.client.get('/user/get/1')
        self.assertEqual(response.status_code, 200)

    def test_show_posts_user_autoriz(self):
        """тестирование метода вывода постов
        авторизованного пользователя с коментариями"""
        response = self.client.get('/user/posts_autot/')
        self.assertEqual(response.status_code, 200)

    def test_show_posts_user(self):
        """тестирование метода вывода постов
                выбранного пользователя с коментариями"""
        response = self.client.get('/user/posts/1')
        self.assertEqual(response.status_code, 200)

    def test_add_posts_user(self):
        """тестирование метода добавления поста пользователя"""
        self.client.login(username='username', password='password')
        response = self.client.post('/user/addpost/', {'title': "title2", 'text': "text2", 'url': "http://url"})
        self.assertEqual(response.status_code, 200)

    def test_edit_post(self):
        """тестирование метода редактирование поста"""
        response = self.client.get('/user/edit/1')
        self.assertEqual(response.status_code, 200)

    def test_savechange(self):
        """тестирование сохранения изменений поста"""
        self.client.login(username='username', password='password')
        response = self.client.post('/user/savechange/', {'post_id': 1, 'title': "title2", 'text': "text2", 'url': "http://url"})
        self.assertEqual(response.status_code, 200)

    def test_addlike(self):
        """тестирование метода добавление лаков"""
        self.client.login(username='username', password='password')
        response = self.client.get('/user/addlike/1')
        self.assertEqual(response.status_code, 302)

    def test_delete_post(self):
        """тестирование метода удаление поста пользователя"""
        response = self.client.get('/user/delete/1')
        self.assertEqual(response.status_code, 200)

    def test_addcomment(self):
        """тестирование метода добавления коментария пользователя"""
        self.client.login(username='username', password='password')
        response = self.client.post('/user/addcomment/1',
                                    {'username': "username", 'text_comment': "text_comment"})
        self.assertEqual(response.status_code, 302)

    def test_delete_comment(self):
        """тестирование метода вывода поста с коментариями"""
        response = self.client.get('/user/deleteComment/1')
        self.assertEqual(response.status_code, 302)
