# Generated by Django 3.2.9 on 2021-12-01 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Answers to FAQs',
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=100)),
                ('website', models.URLField(default='example.com', max_length=500)),
                ('logo', models.ImageField(upload_to='uploads/client_logos/')),
            ],
            options={
                'verbose_name_plural': 'Organisations & Clients',
            },
        ),
        migrations.CreateModel(
            name='CoreValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('title', models.CharField(blank=True, default='title', max_length=255)),
                ('content', models.CharField(default='content', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Core Values',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=100)),
                ('floor', models.CharField(help_text='e.g 3rd,4th,2nd', max_length=15)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Our Location',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('snipet', models.ImageField(blank=True, null=True, upload_to='uploads/patnership_snipets/')),
            ],
            options={
                'verbose_name_plural': 'MSS WeighBridge Services',
            },
        ),
        migrations.CreateModel(
            name='Service_Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('overview', models.TextField(default='classicficatio description', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Service Classification',
            },
        ),
        migrations.CreateModel(
            name='Service_modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_title', models.CharField(default='module #2', max_length=100)),
                ('module_subtitle', models.CharField(default='module #2 subtile', max_length=255)),
                ('module_content', models.TextField(default='module #2 content', max_length=1500)),
            ],
            options={
                'verbose_name_plural': 'Service Modules',
            },
        ),
        migrations.CreateModel(
            name='Social_links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.URLField(default='https://facebook.com', max_length=255)),
                ('icon', models.CharField(blank=True, help_text='use font awesome icons e.g fas fa-tweeter or fa fa-facebook', max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Social Media Links',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField(default='Service short description here...', max_length=255)),
                ('image', models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='uploads/services/')),
                ('icon', models.CharField(max_length=255)),
                ('Service_modules', models.ManyToManyField(blank=True, null=True, to='masterspace.Service_modules')),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='masterspace.service_classification')),
            ],
            options={
                'verbose_name_plural': 'MSS Services',
            },
        ),
        migrations.CreateModel(
            name='FAQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=255)),
                ('answers', models.ManyToManyField(to='masterspace.Answers')),
            ],
            options={
                'verbose_name_plural': 'FAQs & QAs',
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.TextField(max_length=500)),
                ('vission', models.TextField(max_length=255)),
                ('mission', models.TextField(max_length=255)),
                ('date_founded', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(default='info@masterspace.co.ke', max_length=254)),
                ('phone', models.CharField(default='+254(0) 773 499 346', help_text='+254{0} xxx xxx xxx', max_length=15)),
                ('careers_url', models.URLField(default='https://careers.masterspace.co.ke/', max_length=255)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterspace.location')),
                ('social_links', models.ManyToManyField(to='masterspace.Social_links')),
            ],
            options={
                'verbose_name_plural': 'About MSS & Contacts',
            },
        ),
    ]
