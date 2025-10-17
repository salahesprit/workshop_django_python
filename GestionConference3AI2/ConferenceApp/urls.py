from django.urls import path
from . import views
from .views import *
urlpatterns= [
    #path("liste/", views.list_conference, name="liste_conference")
        path("liste/",ConferenceList.as_view(),name="liste_conference"),
        path("<int:pk>",ConferenceDetails.as_view(),name="detail_conference"),
        path("add/",ConferenceCreate.as_view(),name="conference_add")
]