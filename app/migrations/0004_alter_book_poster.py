# Generated by Django 4.0.2 on 2022-02-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='poster',
            field=models.ImageField(null=True, upload_to='books/', verbose_name="photo of book's front"),
        ),
    ]
