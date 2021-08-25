from django.contrib import admin
from .models import Drugstore, Schedule, UserProfile

# Register your models here.
admin.site.register(Drugstore)
admin.site.register(Schedule)
admin.site.register(UserProfile)