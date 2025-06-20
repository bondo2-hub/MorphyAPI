from django.contrib import admin
from django.conf import settings
from .models import User

@admin.register(User)
class MorphyUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'username']
    list_editable = ['gender']
    list_filter = ['gender']