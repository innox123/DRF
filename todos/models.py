from django.db import models


class todos(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.title
