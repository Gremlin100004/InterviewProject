from django.shortcuts import render, redirect
from .models import Posts, Comments, Likes_Post
from django.contrib import auth
from django.utils import timezone
from rest_framework import viewsets
from .serializers import PostsSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

def show_posts(request):
    ctx = {}
    flg_list = []
    posts = Posts.objects.all().order_by('-post_date')
    likes = Likes_Post.objects.all()
    username = auth.get_user(request).username
    for post in posts:
        flag_user = '0'
        flag_url = '0'

        if ('http' in post.post_url) == True:
            flag_url = '1'

        for like in likes:
            if like.likes_post_id == post.id and like.like_user == username:
                flag_user = '1'

        class Flag_post():
            id = post.id
            flag_like = flag_user
            flag_post_url = flag_url

        flg_list.append(Flag_post)

    ctx['show_posts'] = 'last'
    ctx['posts'] = posts
    ctx['likes'] = likes
    ctx['username'] = username
    ctx['posts_flgs'] = flg_list
    return render(request, 'Posts/posts.html', ctx)

def show_posts_top(request):
    ctx = {}
    flg_list = []
    posts = Posts.objects.all().order_by('-number_likes', '-post_date')
    likes = Likes_Post.objects.all()
    username = auth.get_user(request).username
    for post in posts:
        flag_user = '0'
        flag_url = '0'

        if ('http' in post.post_url) == True:
            flag_url = '1'

        for like in likes:
            if like.likes_post_id == post.id and like.like_user == username:
                flag_user = '1'

        class Flag_post():
            id = post.id
            flag_like = flag_user
            flag_post_url = flag_url

        flg_list.append(Flag_post)

    ctx['posts'] = posts
    ctx['likes'] = likes
    ctx['username'] = username
    ctx['posts_flgs'] = flg_list
    ctx['show_posts'] = 'top'
    return render(request, 'Posts/posts.html', ctx)

def show_post_comments(request, post_id=1):
    ctx = {}
    flg_list = []
    username = auth.get_user(request).username
    all_posts = Posts.objects.all()
    post = Posts.objects.get(id=post_id)
    likes = Likes_Post.objects.all()
    flag_like = '0'
    flag_url = '0'
    for like in likes:
        if like.likes_post_id == post_id and like.like_user == username:
            flag_like = '1'
    coment = Comments.objects.filter(comments_article_id=post_id)
    for com in coment:
        class Flag_post():
            id = ''
            id_user_coment = ''
        for post_data in all_posts:
            if post_data.user == com.user:
                Flag_post.id = com.id
                Flag_post.id_user_coment = post_data.id
                break
        flg_list.append(Flag_post)

    if ('http' in post.post_url) == True:
        flag_url = '1'
    ctx['like_flag'] = flag_like
    ctx['post'] = post
    ctx['comments'] = coment
    ctx['username'] = username
    ctx['flag_url'] = flag_url
    ctx['posts_flgs'] = flg_list
    return render(request, 'Posts/post.html', ctx)


def show_posts_user_autoriz(request):
    ctx = {}
    flg_list = []
    posts = Posts.objects.all().order_by('-post_date')
    likes = Likes_Post.objects.all()
    username = auth.get_user(request).username
    for post in posts:
        flag_user = '0'
        flag_url = '0'

        if ('http' in post.post_url) == True:
            flag_url = '1'

        for like in likes:
            if like.likes_post_id == post.id and like.like_user == username:
                flag_user = '1'

        class Flag_post():
            id = post.id
            flag_like = flag_user
            flag_post_url = flag_url

        flg_list.append(Flag_post)

    ctx['posts'] = posts
    ctx['likes'] = likes
    ctx['username'] = username
    ctx['posts_flgs'] = flg_list
    ctx['user_flag'] = 1
    return render(request, 'Posts/UserPosts.html', ctx)

def show_posts_user(request, post_id):
    ctx = {}
    flg_list = []
    posts = Posts.objects.all().order_by('-post_date')
    likes = Likes_Post.objects.all()
    post_user = Posts.objects.get(id=post_id)
    username = post_user.user
    for post in posts:
        flag_user = '0'
        flag_url = '0'

        if ('http' in post.post_url) == True:
            flag_url = '1'

        for like in likes:
            if like.likes_post_id == post.id and like.like_user == username:
                flag_user = '1'

        class Flag_post():
            id = post.id
            flag_like = flag_user
            flag_post_url = flag_url


        flg_list.append(Flag_post)
    if username == auth.get_user(request).username:
        ctx['user_flag'] = 1
    else:
        ctx['user_flag'] = 0
    ctx['posts'] = posts
    ctx['likes'] = likes
    ctx['username'] = username
    ctx['posts_flgs'] = flg_list
    return render(request, 'Posts/UserPosts.html', ctx)


def add_posts_user(request):
    if request.POST:
        username = auth.get_user(request).username
        post_title = request.POST.get('title', '')
        post_text = request.POST.get('text', '')
        post_url = request.POST.get('url', '')
        post_date = timezone.now()
        try:
            post_img = request.FILES['load__img']
        except:
            post_img = None
        model_posts = Posts(user=username, post_title=post_title, post_text=post_text, post_url=post_url,
                            post_date=post_date, post_image=post_img)
        model_posts.save()
        ctx = {}
        posts = Posts.objects.all().order_by('-post_date')
        ctx['posts'] = posts
        ctx['username'] = username
        ctx['user_flag'] = 1
        return render(request, 'Posts/UserPosts.html', ctx)


def edit_post(request, post_id):
    ctx = {}
    Post_user = Posts.objects.get(id=post_id)
    ctx['post'] = Post_user
    ctx['post_id'] = post_id
    return render(request, 'Posts/Edit_post.html', ctx)

def savechange(request):
    if request.POST:
        ctx = {}
        post_id = int(request.POST.get('post_id', ''))
        Post_user = Posts.objects.get(id=post_id)
        Post_user.post_title = request.POST.get('title', '')
        Post_user.post_text = request.POST.get('text', '')
        img_path = request.FILES['load__img'] if 'load__img' in request.FILES else False
        if img_path != False:
            Post_user.post_image = request.FILES['load__img']
        Post_user.post_url = request.POST.get('url', '')
        Post_user.save()
        posts = Posts.objects.get(id=post_id)
        coment = Comments.objects.filter(comments_article_id=post_id)
        ctx['post'] = posts
        ctx['comments'] = coment
        ctx['username'] = auth.get_user(request).username
        return render(request, 'Posts/post.html', ctx)

def delete_post(request, post_id):
    Posts.objects.filter(id=post_id).delete()
    ctx = {}
    flg_list = []
    posts = Posts.objects.all().order_by('-post_date')
    likes = Likes_Post.objects.all()
    username = auth.get_user(request).username
    for post in posts:
        flag_user = '0'
        for like in likes:
            if like.likes_post_id == post.id and like.like_user == username:
                flag_user = '1'

        class Flag_post():
            id = post.id
            flag_like = flag_user

        flg_list.append(Flag_post)

    ctx['posts'] = posts
    ctx['likes'] = likes
    ctx['username'] = username
    ctx['posts_flgs'] = flg_list
    return render(request, 'Posts/UserPosts.html', ctx)

def addlike(request, post_id):
    flg_user = False
    username = auth.get_user(request).username
    post = Posts.objects.get(id=post_id)
    likes = Likes_Post.objects.all()
    for like in likes:
        if like.likes_post_id == post_id and like.like_user == username:
            flg_user = True
            like.delete()
            post.number_likes -= 1
            post.save()
    if flg_user == False:
        model_Likes = Likes_Post(like_user=username, likes_post_id=post_id)
        post.number_likes += 1
        model_Likes.save()
        post.save()
    return redirect("/get/%s" % post_id)


def addcomment(request, post_id):
    if request.POST:
        username = request.POST.get('username', '')
        comments_text = request.POST.get('text_comment', '')
        comments_article = Posts.objects.get(id=post_id)
        model_comments = Comments(user=username, comments_text=comments_text, comments_article=comments_article)
        model_comments.save()
    return redirect('/get/%s' % post_id)

def delete_comment(request, post_id):
    Comments.objects.filter(id=post_id).delete()
    return redirect('/get/%s' % post_id)
