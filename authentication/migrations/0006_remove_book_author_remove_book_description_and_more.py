# Generated by Django 4.0.6 on 2022-08-09 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_book_author_alter_book_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='DESCRIPTION',
        ),
        migrations.RemoveField(
            model_name='book',
            name='GENRE',
        ),
    ]
