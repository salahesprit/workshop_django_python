from django import forms
from .models import Conference
from .models import Submission
class ConferenceForm(forms.ModelForm):
    class Meta:
        model=Conference
        fields=['name','theme','location','desciption','start_date','end_date']
        labels={
            'name':"titre de la conference ",
            'theme':"Thematique de la conference",
        }
    widgets={
        'name' :forms.TextInput(
            attrs={
               'placeholder' :"entrez  la liste des conference "
            }
        ),
        'start_date' :forms.DateInput(
            attrs={
                'type':"date"
            }
        ),
        'end_date' :forms.DateInput(
            attrs={
                'type':"date"
            }
        ),
    }
class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'abstract', 'keywords', 'paper', 'conference', 'payed','status']  