from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ThirdPartyLinks, User

admin.site.register(User, UserAdmin)
admin.site.register(ThirdPartyLinks)
