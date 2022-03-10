# Generated by Django 4.0.2 on 2022-02-15 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ManyToManyField(null=True, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='followers of this author')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_author', to=settings.AUTH_USER_MODEL, verbose_name='user that is an author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name="book's genre")),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name="book's title")),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author', verbose_name='author that wrote this book')),
                ('genre', models.ManyToManyField(to='app.Genre', verbose_name="book's genre")),
            ],
        ),
    ]
