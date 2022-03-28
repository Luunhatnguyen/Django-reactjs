from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.conf import settings
import datetime

class User(AbstractUser):
    pass

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    image = models.ImageField(("Image"), upload_to=upload_to, default='posts/default.jpg')
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=datetime.timezone)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

#db management

class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department(ModelBase):
    name_tourguide = models.TextField()
    address = models.TextField()
    phone = models.TextField()

    def __str__(self):
        return self.name_tourguide

class TourGuide(ModelBase):
    name_tourguide = models.TextField()
    address = models.TextField()
    phone = models.TextField()

    department = models.ForeignKey(Department, related_name="Department", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name_tourguide

class Tour(ModelBase):
    name_tour = models.TextField()
    address = models.TextField()
    phone = models.TextField()

    tourguide = models.ForeignKey(TourGuide, related_name="Tour", null=True, on_delete=models.SET_NULL)
    customer = models.ManyToManyField('Customer')
    hotel = models.ManyToManyField('Hotel')
    transport = models.ManyToManyField('Transport')
    arrival = models.ManyToManyField('Arrival')

    def __str__(self):
        return self.name_tour

class Ticket(ModelBase):
    name_ticket = models.TextField()

    department = models.ForeignKey(Department, related_name="department", null=True, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, related_name="tour", null=True, on_delete=models.SET_NULL)
    customer = models.ManyToManyField('Customer')

    def __str__(self):
        return self.name_ticket

class Customer(ModelBase):
    name_customer = models.TextField()
    address = models.TextField()
    iden = models.TextField()

    def __str__(self):
        return self.name_customer

class Hotel(ModelBase):
    name_hotel = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name_hotel

class Transport(ModelBase):
    name_transport = models.TextField()
    seat = models.CharField(max_length=100)

    def __str__(self):
        return self.name_transport


class Arrival(ModelBase):
    name_arrival = models.TextField()
    address = models.TextField()

    hotel = models.ForeignKey(Hotel, related_name="hotel", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name_arrival
