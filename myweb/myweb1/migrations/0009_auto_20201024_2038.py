# Generated by Django 3.1.2 on 2020-10-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb1', '0008_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image1',
            field=models.ImageField(default='', upload_to='image/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image2',
            field=models.ImageField(default='', upload_to='image/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image3',
            field=models.ImageField(default='', upload_to='image/'),
        ),
    ]