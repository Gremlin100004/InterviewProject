from django.db import models


class Posts(models.Model):
    class Meta():
        db_table = 'posts'
    
    user = models.CharField(max_length=200)
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_date = models.DateTimeField()
    post_url = models.CharField(max_length=200, default=None)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение',)
    number_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title

class Likes_Post(models.Model):
    class Meta():
        db_table = 'likes'

    like_user = models.CharField(max_length=200)
    likes_post = models.ForeignKey('Posts', on_delete=models.CASCADE)

class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField()
    comments_article = models.ForeignKey('Posts', on_delete=models.CASCADE)
    user = models.CharField(max_length=200)