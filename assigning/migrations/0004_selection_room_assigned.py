# Generated by Django 2.2.24 on 2021-08-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assigning', '0003_remove_selection_room_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='selection',
            name='room_assigned',
            field=models.ManyToManyField(to='assigning.Rooms'),
        ),
    ]
