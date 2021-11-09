# Generated by Django 3.2.9 on 2021-11-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterspace', '0013_team_bod_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/cms_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='team',
            name='bod_status',
            field=models.BooleanField(default=False, help_text='Board member or management team official?'),
        ),
        migrations.AlterField(
            model_name='team',
            name='rank',
            field=models.CharField(help_text='Job title e.g CEO,COO,CTO,Director,HR Director', max_length=100),
        ),
    ]
