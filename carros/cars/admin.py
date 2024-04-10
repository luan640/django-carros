from django.contrib import admin

from .models import Car,Brand,Color

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year')
    search_fields = ('model',)
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Color)