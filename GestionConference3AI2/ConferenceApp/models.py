from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator
from django.utils import timezone
import uuid
import random, string
# Create your models here.

class Conference(models.Model):#modifier le comportement de la classe 
    conference_id=models.AutoField(primary_key=True)
    name_validators=RegexValidator(
    regex=r'^[a-zA-Z\s]+$',
    message="le titre de la conférence doit contenir uniquement des lettres et espaces (pas de chiffres).",
)
    name=models.CharField(max_length=255,validators=[name_validators])
    THEME=[
        ("IA","computer science & ia"),
        ("SE","Science & eng"),
        ("SC","Social sciences"),
        ("IT","interdiscriplinary Themes")
    ]
    theme=models.CharField(max_length=255,choices=THEME)
    location=models.CharField(max_length=50)
    desciption=models.TextField(validators=[MinLengthValidator(30,"la description doit contenir au moins 30 caractéres")])
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"la conference a comme titre{self.name}"
    def clean(self):
        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                raise ValidationError("la date de fin doit etre superieur a la date de debut")
                
def validate_keywords(value):
    
     # Séparer les mots-clés par virgule et supprimer les espaces
    keywords = [kw.strip() for kw in value.split(',') if kw.strip()]
    if len(keywords) > 10:
        raise ValidationError("Vous ne pouvez pas saisir plus de 10 mots-clés.")

def generate_submission_id():
    return "USB-"+uuid.uuid4().hex[:8].upper()

class Submission (models.Model):
    submission_id=models.CharField(max_length=255,primary_key=True,unique=True,editable=False)
    title=models.CharField(max_length=255)
    abstract=models.TextField() 
    keywords=models.TextField(max_length=255, validators=[validate_keywords])
    paper=models.FileField(
        upload_to="paper/",
         validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf'],
                message="Seuls les fichiers au format .pdf sont autorisés."
            )
        ]
    )
    STATUS=[
        ("submitted","submitted"),
        ("under review","under review"),
        ("accepted","accepted"),
        ("rejected","rejected"),
    ]
    status=models.CharField(max_length=50,choices=STATUS)
    payed=models.BooleanField(default=False)
    submission_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="submissions")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE, related_name="submissions")
    def clean(self):
        '''
        if self.submission_date:
        # 1️⃣ Vérifier que la conférence est à venir
            if self.conference.start_date < timezone.now().date() and self.submission_date>self.conference.start_date:
                raise ValidationError({
                    'conference': "La soumission ne peut être faite que pour des conférences à venir."
                })

        # 2️⃣ Limiter le nombre de soumissions par utilisateur et par jour
        today = timezone.now().date()

        existing_submissions = Submission.objects.filter(
            user=self.user,
            submission_date__date=today
        )
        if self.pk:
            existing_submissions = existing_submissions.exclude(pk=self.pk)

        if existing_submissions.count() >= 3:
            raise ValidationError(
                f"Vous avez déjà atteint le nombre maximal de 3 soumissions pour la date du {today}."
            )
        
        """keywords_list=[]
        if self.keywords:
            for k in self.keywords.split(","):
                k=k.strip()
                if k:
                    keywords_list.append(k)"""
'''
        # 🔹 Vérification dates : uniformiser date/datetime
        if self.conference and self.conference.start_date and self.submission_date:
            start_date = self.conference.start_date
            submission_date = self.submission_date.date()  # convert datetime -> date
            if start_date < timezone.now().date() and submission_date > start_date:
                raise ValidationError("La soumission ne peut être faite que pour des conférences à venir.")

        # 🔹 Vérification mots-clés
        keyword_list = []
        if self.keywords:
            for k in self.keywords.split(","):
                k = k.strip()
                if k:
                    keyword_list.append(k)
                    if len(keyword_list) > 10:
                        raise ValidationError({"keywords": "Vous ne pouvez pas saisir plus de 10 mots-clés."})

        # 🔹 Limite de soumissions par jour
        if self.user_id:
            today = timezone.now().date()
            submissions_today = Submission.objects.filter(
                user=self.user,
                submission_date__date=today
            ).count()
            if submissions_today >= 3 and not self.pk:  # exclude if updating
                raise ValidationError("Vous ne pouvez pas soumettre plus de 3 conférences par jour.")
    '''       
    def save(self, *args, **kwargs): #*args is for a format of a tuple and **kwargs is  for a format of a dictionary
         if not self.submission_id:
            newid = generate_submission_id()
            while Submission.objects.filter(submission_id=newid).exists():#tantque que le newid existe dans la base de donnee on genere un autre
                newid = generate_submission_id()
            self.submission_id=newid
            self.full_clean()  # appelle clean() avant chaque sauvegarde
            super().save(*args,**kwargs) '''
    def save(self, *args, **kwargs):
        if not self.submission_id:
            random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            self.submission_id = f"SUB-{random_part}"
        if hasattr(self, "user") and self.user is not None:
            self.full_clean()  # Call validations before saving
        super().save(*args, **kwargs)    