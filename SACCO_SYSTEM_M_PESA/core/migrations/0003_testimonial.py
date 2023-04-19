# Generated by Django 4.0.4 on 2022-05-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to='')),
                ('message', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]