# Generated by Django 2.2.5 on 2019-10-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
