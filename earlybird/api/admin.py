from django.contrib import admin

from .models import Account, History, Rank

admin.site.register(Account)
admin.site.register(History)
admin.site.register(Rank)
