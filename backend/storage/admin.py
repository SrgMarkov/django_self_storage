from django.contrib import admin
# from backend.storage.models import Stock, BoxX, UserProfile
from storage.models import Stock, BoxX, UserProfile, Lead


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'property', 'capacity')


@admin.register(BoxX)
class BoxXAdmin(admin.ModelAdmin):
    list_display = ('box_number', 'create_date')

    def create_data_display(self, obj):
        return obj.create_time.strftime("%B %d, %Y")

    create_data_display.short_description = 'Дата'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('eMail', 'address')

