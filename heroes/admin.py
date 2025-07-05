from django.contrib import admin
from .models import SuperHeroes

# Register your models here.
class heroadmin(admin.ModelAdmin):
    list_display = ("name", "city", "super_hero_name")
    prepopulated_fields = {'slug':('super_hero_name',)}

admin.site.register(SuperHeroes, heroadmin)