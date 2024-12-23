# Generated by Django 4.2.16 on 2024-11-29 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_collaboraterequest_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaboraterequest',
            name='message',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(1, 'The message must have at least 1 character.'), django.core.validators.MaxLengthValidator(2000, 'The message cannot exceed 2000 characters.')]),
        ),
    ]
