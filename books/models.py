from django.contrib.auth.models import Permission, User
from django.db import models
from django.urls import reverse


class Book(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.PROTECT)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=1000)
    publisher = models.CharField(max_length=500)
    type = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    book = models.FileField(default=1)
    cover = models.FileField()

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + '-' + self.author
