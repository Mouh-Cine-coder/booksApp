# Generated by Django 4.2.5 on 2023-09-26 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_book_language_alter_book_num_pages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]
