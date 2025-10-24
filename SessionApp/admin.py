from django.contrib import admin
from .models import Session
# Register your models here.
#admin.site.register(Session)
@admin.register(Session)
class admin_Session_model(admin.ModelAdmin):
    list_display = ("title", "topic", "session_day", "start_time", "end_time", "room", "a")
    ordering = ("session_day", "start_time")
    search_fields = ("title", "topic", "room")
    list_filter = ("topic", "session_day")
    date_hierarchy = "session_day"

    fieldsets = (
        ("Informations générales", {
            "fields": ("session_id", "title", "topic", "conference")
        }),
        ("Détails de planification", {
            "fields": ("session_day", "start_time", "end_time", "room")
        }),
    )

    readonly_fields = ("session_id",)

    def a(self, objet):
        if objet.start_time and objet.end_time:
            duration = (
                (objet.end_time.hour * 60 + objet.end_time.minute)
                - (objet.start_time.hour * 60 + objet.start_time.minute)
            )
            hours = duration // 60
            minutes = duration % 60
            return f"{hours}h {minutes}min"
        return "RAS"

    a.short_description = "Durée"