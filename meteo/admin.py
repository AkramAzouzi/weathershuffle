from django.contrib import admin
from .models import Worldcities


@admin.register(Worldcities)
class WorldcitiesAdmin(admin.ModelAdmin):
    list_display = ["city", "lat", "lng", "country", "id"]
    list_filter = ["country"]
    search_fields = ["city", "country"]
    readonly_fields = ["id"]
