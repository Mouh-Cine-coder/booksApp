# Generated by Django 4.2.5 on 2023-09-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customer_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='imagesUsers/'),
        ),
    ]
