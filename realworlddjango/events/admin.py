from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Event)
class BrandAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Category)
class BrandAdmin(admin.ModelAdmin):
  pass