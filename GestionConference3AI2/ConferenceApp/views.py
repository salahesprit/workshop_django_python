from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView
from django.views.generic import DetailView ,CreateView 
from django.urls import reverse_lazy
# Create your views here.


def list_conference(request):
    liste_conference=Conference.objects.all()
    """retour : liste + page html """
    return render(request,"conference/liste.html",{"liste":liste_conference})
class ConferenceList(ListView):
    model=Conference
    context_object_name="liste"
    template_name="conference/liste.html"
class ConferenceDetails(DetailView):
    model=Conference
    context_object_name="Conference"
    template_name="conference/detail.html"
class ConferenceCreate(CreateView):
    model=Conference
    template_name="conference/form.html"
    context_object_name="Conference"
    fields="__all__"
    success_url=reverse_lazy("liste_conference")