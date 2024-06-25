from django import forms
from .models import Consultation
from .models import Register
from .models import ContactSubmission

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields='__all__'
        
class RegisterForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Register                                         
        fields='__all__'

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Register
        fields=('Email','Password')

class UpdateForm(forms.ModelForm):
    class Meta():
        model=Register
        fields=('Name','phone','Email')
        
class ChangepasswordForm(forms.ModelForm):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    
class ContactForm(forms.ModelForm):
    class Meta():
        model = ContactSubmission
        fields=('name','email','message')