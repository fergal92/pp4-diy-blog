# Generated by Django 4.2.16 on 2024-11-29 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaboraterequest',
            name='message',
            field=models.TextField(max_length=2000),
        ),
    ]
