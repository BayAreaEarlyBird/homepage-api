from django.contrib import admin

from problem_solving.models import LeetcodeSolvedNumberRecord, RankRecord

admin.site.register(RankRecord)
admin.site.register(LeetcodeSolvedNumberRecord)
