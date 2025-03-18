from django.db import models


class Post(models.Model):
    location = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f'{self.date} - {self.location}'
