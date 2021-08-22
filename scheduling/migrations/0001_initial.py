# Generated by Django 2.2.24 on 2021-08-22 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_upload', models.ImageField(blank=True, null=True, upload_to='noticeUpload/')),
                ('description', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=50, verbose_name='first_Name')),
                ('last_Name', models.CharField(max_length=50, verbose_name='last_Name')),
                ('gender', models.CharField(max_length=5, verbose_name='gender')),
                ('age', models.CharField(max_length=3, verbose_name='age')),
                ('email_Id', models.CharField(max_length=20, verbose_name='email_Id')),
                ('phone_Num', models.CharField(max_length=10, verbose_name='phone_Num')),
            ],
        ),
        migrations.CreateModel(
            name='Selected_person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.Person')),
            ],
        ),
    ]
