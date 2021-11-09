# Generated by Django 3.2.9 on 2021-11-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterspace', '0007_auto_20211106_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='featured',
        ),
        migrations.AddField(
            model_name='services',
            name='classification',
            field=models.CharField(choices=[('Featured', 'Featured'), ('Core', 'Core'), ('New', 'New')], default='Featured', max_length=20),
        ),
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/services/'),
        ),
    ]
