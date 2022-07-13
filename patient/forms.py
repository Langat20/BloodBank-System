from django import forms
from django.contrib.auth.models import User
from . import models


class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class PatientForm(forms.ModelForm):
    
    class Meta:
        model=models.Patient
<<<<<<< HEAD
        fields=['age','bloodgroup','disease','emailaddress','doctorname','mobile','profile_pic']
=======
        fields=['age','bloodgroup','disease','address','doctorname','mobile','image']
>>>>>>> 968e2f3ede6ecbc90af6a613fca2991231ab086a
