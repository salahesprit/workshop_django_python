from django.contrib import admin
from .models import User ,Organizing_Committee
# Register your models here.
#admin.site.register(User)
#admin.site.register(Organizing_Committee)
class OrganizingCommitteeInline(admin.StackedInline):
    model = Organizing_Committee
    extra = 1
    readonly_fields = ["created_at", "update_at"]

@admin.register(User)
class AdminUserModel(admin.ModelAdmin):
    list_display = ("user_id","first_name","last_name","email","role","affiliation_short","nationality","created_at",)

    def affiliation_short(self, obj):
        if len(obj.affiliation) > 30:
            return obj.affiliation[:30] + "..."
        return obj.affiliation
    affiliation_short.short_description = "Affiliation (court)"

    list_filter = ("role", "nationality", "created_at")
    search_fields = ("first_name", "last_name", "email", "user_id", "affiliation")
    fieldsets = (
        ("Informations générales", {
            "fields": ("user_id", "first_name", "last_name", "email", "role", "affiliation")
        }),
        ("Détails supplémentaires", {
            "fields": ("nationality",)
        }),
    )
    readonly_fields = ("user_id",)

    inlines = [OrganizingCommitteeInline]  # <-- ici on ajoute le TabularInline

@admin.register(Organizing_Committee)
class AdminOrganizingCommittee(admin.ModelAdmin):
    list_display = ("user_full_name","committee_role","conference","date_joined",)

    def user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    user_full_name.short_description = "Nom du membre"

    list_filter = ("committee_role", "conference", "date_joined")
    search_fields = ("user__first_name", "user__last_name", "conference__name")
    
    fieldsets = (
        ("Informations sur le membre", {
            "fields": ("user", "committee_role", "date_joined")
        }),
        ("Audit", {
            "fields": ("created_at", "update_at", "conference")
        }),
    )

    readonly_fields = ("created_at", "update_at")