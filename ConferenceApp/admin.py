from django.contrib import admin
from .models import Conference, Submission
# Register your models here.
admin.site.site_title="Gestion de Conférence25-26"
admin.site.site_header="Administration de Conférence"
admin.site.index_title="django app conference"
#admin.site.register(Conference)
#admin.site.register(Submission)
class Submission_inline(admin.TabularInline): #ou StackedInline pour le un bloc 
    model = Submission
    extra = 1
    readonly_fields=["submission_date"]
@admin.register(Conference)
class admin_Conference_model(admin.ModelAdmin):
    list_display=("name","theme","location","start_date","end_date","a")
    ordering=("start_date",)
    search_fields=("name","theme","desciption")
    list_filter=("theme",)
    date_hierarchy="start_date"
    fieldsets=(
        ("information general",{
            "fields":("conference_id","name","theme","desciption")
        }),
        ("logistique Info",
         {
             "fields":("location","start_date","end_date")
         }),
    )
    readonly_fields=("conference_id",)
    def a(self,objet):
        if objet.start_date and objet.end_date:
            return (objet.end_date-objet.start_date).days
        return "RAS"
    a.short_description="Duration (days)"
    inlines=[Submission_inline]
@admin.action(description="marker comme payer")
def marked_as_payed(modeladmin,req,queryset):
    queryset.update(payed=True)
@admin.action(description="marked as requested")
def marked_as_requested(modeladmin,req,queryset):
    queryset.update(status="accepted")
@admin.register(Submission)
class admin_Submission_model(admin.ModelAdmin):
    list_display=("title","status","user","conference","submission_date","payed","a")
    def a(self, object):
        if len(object.abstract) > 50:
            return object.abstract[:50] + '...'
        return object.abstract
    a.short_description = 'Abstract (court)'
    list_filter = ('status', 'payed', 'conference', 'submission_date')
    search_fields = ('title', 'conference__name', 'user__username')
    list_editable = ('status', 'payed')
    fieldsets = (
        ('Infos générales', {
            'fields': ('submission_id', 'title', 'abstract', 'keywords')
        }),
        ('Fichier et conférence', {
            'fields': ('paper', 'conference')
        }),
        ('Suivi', {
            'fields': ('status', 'payed', 'submission_date', 'user')
        }),
    )
    readonly_fields = ('submission_id', 'submission_date') 
    actions=[marked_as_payed,marked_as_requested]