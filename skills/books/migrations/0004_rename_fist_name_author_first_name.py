# Generated by Django 4.0.3 on 2022-03-31 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]
