# Generated by Django 3.2.9 on 2021-11-23 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterspace', '0024_clients_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/teams/'),
        ),
    ]