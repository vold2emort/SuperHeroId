from django.db import models

# Create your models here.
class SuperHeroes(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    super_hero_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.name}"