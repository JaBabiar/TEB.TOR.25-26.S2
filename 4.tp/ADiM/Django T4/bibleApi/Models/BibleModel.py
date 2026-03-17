from django.db import models


class Verse(models.Model):
    author = models.CharField(max_length=64)
    verse = models.TextField("Verse")