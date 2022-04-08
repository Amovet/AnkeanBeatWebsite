from django.contrib import admin
from .models import PlayList
# Register your models here.


class AnkeanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'bpm', 'link')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('id', 'title', 'price', 'bpm')


admin.site.register(PlayList, AnkeanAdmin)
