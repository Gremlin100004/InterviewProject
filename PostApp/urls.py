from django.urls import path
from PostApp import views
from django.conf import settings

urlpatterns = [
    path('', views.show_posts),
    path('top/', views.show_posts_top),
    path('get/<int:post_id>', views.show_post_comments, name='post'),
    path('edit/<int:post_id>', views.edit_post, name='edit post'),
    path('delete/<int:post_id>', views.delete_post, name='delete post'),
    path('deleteComment/<int:post_id>', views.delete_comment, name='delete post'),
    path('savechange/', views.savechange, name='save change post'),
    path('addlike/<int:post_id>', views.addlike, name='add like'),
    path('addcomment/<int:post_id>', views.addcomment, name='add new comment'),
    path('posts/<int:post_id>', views.show_posts_user, name='user posts'),
    path('posts_autot/', views.show_posts_user_autoriz, name='user posts'),
    path('addpost/', views.add_posts_user, name='user posts'),
]
