from django.contrib import admin
from accounts.models import User, Country, City


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'dni', 'country', 'phone')
    search_fields = ('username', 'first_name', 'last_name', 'dni')
    list_filter = ('dni',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(User, UserAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
