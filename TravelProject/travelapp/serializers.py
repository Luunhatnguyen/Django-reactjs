from rest_framework import serializers
from .models import User, Post

class UserSerializers(serializers.ModelSerializer):
    # ghi de lai de bam mk
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)    #bam mk
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'password', 'email', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'image', 'slug', 'author',
                  'excerpt', 'content', 'status')