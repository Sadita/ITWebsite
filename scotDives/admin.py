from django.contrib import admin
from .models import DiveSpot, DiveClub, DiveSite


class DiveSiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(DiveSpot)
admin.site.register(DiveClub)
admin.site.register(DiveSite)
# Register your models here.
