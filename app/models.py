from django.db import models


# Create your models here.
class AuthorModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, help_text="author name")
    email = models.CharField(max_length=100, blank=True, null=True, help_text="author email")
    publish_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, help_text="book name")
    description = models.TextField(blank=True, null=True, help_text="book description")
    image = models.ImageField(blank=True, null=True, help_text="book image")
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    publish_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
