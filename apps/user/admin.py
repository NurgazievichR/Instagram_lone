import copy
from django.contrib import admin

from apps.user.models import CustomUser

admin.site.register(CustomUser)
