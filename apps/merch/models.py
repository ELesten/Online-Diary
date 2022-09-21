from django.db import models


class Merch(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    count = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
