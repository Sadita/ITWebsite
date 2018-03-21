from django.contrib import admin
from .models import DiveClub, DiveSite, Picture, UserProfile, FutureDive, Review


class DiveSiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(DiveClub)
admin.site.register(DiveSite)
admin.site.register(Picture)
admin.site.register(UserProfile)
admin.site.register(FutureDive)
admin.site.register(Review)
# Register your models here.
