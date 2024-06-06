from django.contrib import admin

from apps.account.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
