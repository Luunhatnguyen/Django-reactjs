# Generated by Django 4.0.4 on 2022-05-02 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0029_remove_tour_image_tour_imagetour'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'ordering': ['-id']},
        ),
    ]
