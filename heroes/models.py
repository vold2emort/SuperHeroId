from django.db import models

# Create your models here.


class SuperHeroes(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, null=True)
    super_hero_name = models.CharField(max_length=100)
    superpower = models.TextField(null=True)
    city = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
