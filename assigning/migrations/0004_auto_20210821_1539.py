# Generated by Django 2.2.24 on 2021-08-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assigning', '0003_auto_20210821_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='selected_persons',
            field=models.ManyToManyField(to='scheduling.Selected_person'),
        ),
    ]
