from django.contrib import admin

from .models import Hero, Item


class HeroAdmin(admin.ModelAdmin):
    list_display = ['name', 'hero_class', 'level', 'creation_data']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']


admin.site.register(Hero, HeroAdmin)
admin.site.register(Item, ItemAdmin)
