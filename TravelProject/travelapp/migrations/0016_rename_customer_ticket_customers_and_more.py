# Generated by Django 4.0.3 on 2022-03-30 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0015_remove_tourguide_phone_alter_department_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='customer',
            new_name='customers',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='arrival',
            new_name='arrivals',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='customer',
            new_name='customers',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='hotel',
            new_name='hotels',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='transport',
            new_name='transports',
        ),
    ]
