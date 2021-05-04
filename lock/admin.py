from django.contrib import admin
from .models import Event, EventMember, KeyInfo, Access, State, HistoryEntered, Equipment
# Register your models here.

@admin.register(EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['event', 'user']
    
@admin.register(KeyInfo)
class KeyInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'key', 'Status']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['display_day', 'display_time']

admin.site.register(Access)
admin.site.register(State)
admin.site.register(HistoryEntered)
admin.site.register(Equipment)