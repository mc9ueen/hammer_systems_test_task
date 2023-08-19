from django.contrib import admin

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phone_number', 'referral_code', 'invite_code',)
    list_editable = ('phone_number', )
    search_fields = ('phone_number', )
    list_filter = ('phone_number', 'referral_code')
    empty_value_display = 'пусто'


admin.site.register(CustomUser, CustomUserAdmin)
