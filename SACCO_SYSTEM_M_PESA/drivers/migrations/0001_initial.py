# Generated by Django 4.0.4 on 2022-05-26 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('First_Name', models.CharField(max_length=100)),
                ('Second_Name', models.CharField(max_length=100)),
                ('ID_No', models.CharField(max_length=100)),
                ('Age', models.PositiveIntegerField()),
                ('Avatar', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Drivers',
            },
        ),
    ]
