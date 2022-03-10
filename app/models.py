from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    """Author of books"""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='user_author',
        verbose_name='user that is an author'
    )
    followers = models.ManyToManyField(
        User, blank=True,
        related_name='followers',
        verbose_name='followers of this author'
    )

    def __str__(self):
        return self.user.username


class Genre(models.Model):
    """Genre of book"""
    title = models.CharField('book\'s genre', max_length=40)

    def __str__(self):
        return self.title


class Book(models.Model):
    """Book that was written by author"""
    title = models.CharField('book\'s title', max_length=30)
    genre = models.ManyToManyField(Genre, verbose_name='book\'s genre')
    draft = models.BooleanField(default=True, verbose_name='is draft')
    poster = models.ImageField('photo of book\'s front',
                               upload_to='books/', null=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE,
        verbose_name='author that wrote this book'
    )

    def __str__(self):
        return self.title
