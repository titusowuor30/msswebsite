# Generated by Django 3.2.9 on 2021-12-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterspace', '0002_alter_corevalues_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='icon',
        ),
        migrations.AlterField(
            model_name='corevalues',
            name='image',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='uploads/corevalues/'),
        ),
        migrations.AlterField(
            model_name='service_classification',
            name='overview',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='service_modules',
            name='module_subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]