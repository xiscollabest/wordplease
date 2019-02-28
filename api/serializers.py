from rest_framework import serializers
from django.contrib.auth.models import User
from blogs.models import Post


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email')

class UserSerializer(UserListSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'first_name', 'last_name', 'email')
    
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class BlogSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField('blog_url')
    posts = serializers.SerializerMethodField('count')

    def blog_url(self, user):
        link = "{}://{}{}{}/".format(self.context['request'].scheme, self.context['request'].get_host(), "/blogs/", user.username)
        return link
    
    def count(self, user):
        return Post.objects.filter(owner=user).count()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'posts', 'url')
