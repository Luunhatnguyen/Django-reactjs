from rest_framework import serializers
from .models import User, Department, Tour, Hotel, Transport, Arrival, Action, Rating, TourGuide
from rest_framework.serializers import ModelSerializer, SerializerMethodField

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(source='avatar')

    # avatar_path = serializers.SerializerMethodField()
    def get_avatar_path(self, user):
        request = self.context['request']
        if user.avatar and not user.avatar.name.startswith('/static'):
            path = '/static/%s' % user.avatar.name

            return request.build_absolute_uri(path)


    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'avatar_path']
        extra_kwargs = {
            'password': {
                'write_only': True
            }, 'avatar_path': {
                'read_only': True
            }, 'avatar': {
                'write_only': True
            }
        }


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('category', 'id', 'title', 'image', 'slug', 'author',
#                   'excerpt', 'content', 'status')

class DepartmentSeriliazer(ModelSerializer):
    class Meta:
        model = Department
        fileds = "__all__"
        exclude = ['active']


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name_hotel']

class ArrivalSerializer(ModelSerializer):
    class Meta:
        model = Arrival
        fields = ['name_arrival', 'address']

class TourguideSerializer(ModelSerializer):
    class Meta:
        model = TourGuide
        fields = ['imageTourGuide', 'department']

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
    # departments = DepartmentSeriliazer(many=True)
    transports = TransportSerializer(many=True)
    hotels = HotelSerializer(many=True)
    arrivals = ArrivalSerializer(many=True)

    def get_image(self, obj):
        pass
    #     request = self.context['request']
    #     if obj.image and not obj.image.name.startswith('/static'):
    #         path = '/static/%s' % obj.image.name
    #
    #         return request.build_absolute_uri(path)

    class Meta:
        model = Tour
        fields = ['name_tour', 'address', 'phone', 'imageTour',
                  'transports', 'hotels', 'image', 'arrivals']


class TourDetailSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = TourSerializer.Meta.fields


class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "type", "create_date"]

class RateSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "type", "create_date"]
