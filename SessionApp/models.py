from django.db import models
from ConferenceApp.models import Conference
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.
class Session(models.Model):
    session_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    topic=models.CharField(max_length=255)
    session_day=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    name_validators=RegexValidator(
    regex=r'^[a-zA-Z0-9]+$',
    message="le nom de la salle ne contient que des lettres et chiffres (pas de caractères spéciaux)",
)
    room=models.CharField(max_length=255,validators=[name_validators])
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    conference=models.ForeignKey("ConferenceApp.conference",on_delete=models.CASCADE,related_name="sessions")#cascarde pour eviter les prrobleme de suppression de foreign key de la table mere (liee a la table mere conference)

    #conference=models.ForeignKey(Conference,on_delete=models.CASCADE)
    def clean(self):
            if self.end_time < self.start_time:
                raise ValidationError("la date de fin doit etre superieur a la date de debut")
        # Vérifie que la conférence existe
            if not (self.conference.start_date <= self.session_day <= self.conference.end_date):
                raise ValidationError({
                    'session_day': f"La date de la session doit être comprise entre "
                                   f"{self.conference.start_date} et {self.conference.end_date}."
                })
    