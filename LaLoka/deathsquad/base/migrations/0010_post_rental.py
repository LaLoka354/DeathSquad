# Generated by Django 5.0.1 on 2024-04-07 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_post_lugar_post_organiza_post_paga'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rental',
            field=models.BooleanField(default=True),
        ),
    ]
