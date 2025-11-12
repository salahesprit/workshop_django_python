from django.shortcuts import render
from .models import Conference
from .models import Submission
from django.views.generic import ListView
from django.views.generic import DetailView ,CreateView 
from django.views.generic import DeleteView ,UpdateView
from django.urls import reverse_lazy
from .forms import ConferenceForm ,SubmissionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
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
class ConferenceCreate(LoginRequiredMixin,CreateView):
    model=Conference
    template_name="conference/form.html"
    context_object_name="Conference"
    #fields="__all__"
    form_class=ConferenceForm
    success_url=reverse_lazy("liste_conference")
class UpdateConference(LoginRequiredMixin,UpdateView):
    model = Conference
    #fields="__all__"
    form_class=ConferenceForm
    template_name = 'conference/form.html'
    success_url = reverse_lazy('liste_conference')  
class DeleteConference(LoginRequiredMixin,DeleteView):
    model = Conference
    template_name = 'conference/delete.html'
    success_url = reverse_lazy('liste_conference')

class SubmissionList(ListView):
    model = Submission
    context_object_name = "liste"
    template_name = "Submissions/liste.html"  
    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user)

class SubmissionDetails(DetailView):
    model = Submission
    context_object_name = "submission"
    template_name = "Submissions/details.html"

class SubmissionCreate(LoginRequiredMixin,CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = "Submissions/form.html"
    success_url = reverse_lazy("submission_list")

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
class SubmissionUpdate(LoginRequiredMixin,UpdateView):
    model = Submission
    form_class = SubmissionForm
    template_name = "Submissions/form.html"
    success_url = reverse_lazy("submission_list")
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['title'].disabled = False
        form.fields['abstract'].disabled = False
        form.fields['keywords'].disabled = False
        form.fields['paper'].disabled = False

        for field in ['conference', 'user', 'submission_id', 'submission_date']:
            if field in form.fields:
                form.fields[field].disabled = True
        return form
    def dispatch(self, request, *args, **kwargs):
        Submission = self.get_object()
        if Submission.status in ['accepted', 'rejected']:
            return HttpResponseForbidden(f"Cette soumission ne peut pas être modifiée car elle est {Submission.status}.")
        return super().dispatch(request, *args, **kwargs)