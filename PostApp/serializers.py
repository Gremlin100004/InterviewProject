from rest_framework import serializers
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'user', 'post_title', 'post_text', 'post_date', 'post_url', 'post_image', 'number_likes')

    user = serializers.CharField(max_length=200)
    post_title = serializers.CharField(max_length=200)
    post_text = serializers.CharField()
    post_date = serializers.DateTimeField()
    post_url = serializers.CharField(max_length=200)
    post_image = serializers.ImageField(default=None)
    number_likes = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Posts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.post_title = validated_data.get('Post title', instance.post_title)
        instance.post_text = validated_data.get('Post text', instance.post_text)
        instance.post_date = validated_data.get('Post date', instance.post_date)
        instance.post_url = validated_data.get('Post url', instance.post_url)
        instance.post_image = validated_data.get('Post image', instance.post_image)
        instance.number_likes = validated_data.get('Number likes', instance.number_likes)

        instance.save()
        return instance


#requests REAST