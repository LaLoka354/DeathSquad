# Generated by Django 5.0.1 on 2024-03-16 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_text_post_descripcion_remove_post_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Lugar',
            new_name='title',
        ),
    ]
