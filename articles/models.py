from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE, blank=True, null=True)