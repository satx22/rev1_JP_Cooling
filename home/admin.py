from django.contrib import admin
from .models import SpecialOfferEmail

@admin.register(SpecialOfferEmail)
class SpecialOfferEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')