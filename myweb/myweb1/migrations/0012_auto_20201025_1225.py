# Generated by Django 3.1.2 on 2020-10-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb1', '0011_auto_20201025_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headtext', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=10)),
                ('contactpic', models.ImageField(default='', upload_to='image/')),
                ('service1', models.CharField(max_length=10)),
                ('service2', models.CharField(max_length=10)),
                ('service3', models.CharField(max_length=10)),
                ('service4', models.CharField(max_length=10)),
                ('service5', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='freepic',
            field=models.ImageField(default='', upload_to='image/'),
        ),
    ]
