from django.contrib import admin
# from backend.storage.models import Stock, BoxX, UserProfile
from storage.models import Stock, BoxX, UserProfile, Lead


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'property', 'capacity')


@admin.register(BoxX)
class BoxXAdmin(admin.ModelAdmin):
    list_display = ('box_number', 'boxx', 'create_date')
    readonly_fields = ('stock_qr_code',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('eMail', 'address')

