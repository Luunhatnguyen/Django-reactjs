from rest_framework import serializers
from .models import User, Post, Department, Tour, Hotel, Transport, Arrival, Action, Rating
from rest_framework.serializers import ModelSerializer

class UserSerializer(serializers.ModelSerializer):
    avatar_path = serializers.SerializerMethodField(source='avatar')

    def get_avatar_path(self, obj):
        request = self.context['request']
        if obj.avatar and not obj.avatar.name.startswith('/static'):
            path = '/static/%s' % obj.avatar.name

            return request.build_absolute_uri(path)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'avatar', 'avatar_path']
        extra_kwargs = {
            'password': {
                'write_only': True
            }, 'avatar_path': {
                'read_only': True
            }, 'avatar': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        data = validated_data.copy()

        u = User(**data)
        u.set_password(u.password)
        u.save()

        return u


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'image', 'slug', 'author',
                  'excerpt', 'content', 'status')

class DepartmentSeriliazer(ModelSerializer):
    class Meta:
        model = Department
        fileds = "__all__"
        exclude = ['active']


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name_hotel']

class TransportSerializer(ModelSerializer):
    class Meta:
        model = Transport
        fields = ['id', 'name_transport', 'seat']

class ArrivalSerializer(ModelSerializer):
    class Meta:
        model = Arrival
        fields = ['id', 'name_arrival']

class TourSerializer(ModelSerializer):
    image = serializers.SerializerMethodField(source='imageTour')
    departments = DepartmentSeriliazer(many=True)
    transports = TransportSerializer(many=True)
    hotels = HotelSerializer(many=True)
    arrivals = ArrivalSerializer(many=True)

    def get_image(self, obj):
        request = self.context['request']
        if obj.image and not obj.image.name.startswith('/static'):
            path = '/static/%s' % obj.image.name

            return request.build_absolute_uri(path)

    class Meta:
        model = Tour
        fields = ['name_tour', 'address', 'phone', 'imageTour',
                  'departments', 'transports', 'hotels', 'imageTour', 'image', 'arrivals']

class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "type", "create_date"]

class RateSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "type", "create_date"]
