from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Reporter(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=500)
    categories = models.ManyToManyField(Category)
    affiliation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    series = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=500)
    published_at = models.DateField()
    published_by = models.ForeignKey(Reporter, related_name='articles', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
