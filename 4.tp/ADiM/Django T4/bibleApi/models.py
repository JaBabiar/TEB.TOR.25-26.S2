from django.db import models

# Create your models here.


class Verse(models.Model):
    author = models.CharField(max_length=64)
    verse = models.TextField("Verse")

    def __str__(self):
        return self.verse