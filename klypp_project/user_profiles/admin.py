from django.contrib import admin
from .models import KlyppUser
from . import models

# Register your models here.
admin.site.register(models.KlyppUser)
