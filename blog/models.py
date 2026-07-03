from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Blog(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to='blog_images/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    views = models.PositiveIntegerField(default=0)

    # ❤️ Like System
    likes = models.PositiveIntegerField(default=0)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name