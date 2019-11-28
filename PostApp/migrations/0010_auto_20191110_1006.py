# Generated by Django 2.2.6 on 2019-11-10 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0009_auto_20191007_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post_likes',
        ),
        migrations.CreateModel(
            name='Likes_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('likes_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PostApp.Posts')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
    ]
