from models import Person, Holiday, Planner
from django.contrib import admin


admin.site.register(Planner)


class HolidayAdmin(admin.ModelAdmin):
    list_filter = ('country', 'destination', 'cost','nrdays' )
    ordering = ('-cost',)
    search_fields = ('country',)

admin.site.register(Holiday,HolidayAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'daysoff')
    ordering = ('-name',)

admin.site.register(Person,PersonAdmin)