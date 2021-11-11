from django.contrib import admin
from .models import Venue
from .models import myClubUser
from .models import Event


#make the tables available in admin section
# admin.site.register(Venue)
admin.site.register(myClubUser)
#admin.site.register(Event)
@admin.register(Venue)
class venueAdmin(admin.ModelAdmin):
     list_display = ('name','address','phone_number','website')
     ordering = ('name',)
     search_fields = ('name','address')
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name','venue'),'event_date','description','manager')
    list_display = ('name','event_date','venue')
    list_filter = ('event_date','venue')
    ordering = ('-event_date',)