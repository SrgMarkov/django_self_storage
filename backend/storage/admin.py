from django.contrib import admin
# from backend.storage.models import Stock, BoxX, UserProfile
from storage.models import Stock, BoxX, UserProfile


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('address', 'property', 'capacity')


@admin.register(BoxX)
class BoxXAdmin(admin.ModelAdmin):
    list_display = ('box_number', 'create_date', 'involved')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')

