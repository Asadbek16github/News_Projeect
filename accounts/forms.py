from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class userRegistrationform(forms.ModelForm):
    username = forms.CharField(label='Foydalanuvchi nomi')
    first_name = forms.CharField(label='Ismingiz')
    last_name = forms.CharField(label='Familyangiz')
    email = forms.EmailField(label='Email manzilingiz')
    age = forms.IntegerField(label='Yoshingiz')
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Parolni tasdiqlang', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'age']

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Ikkita prol bir biriga teng emas !')
        return data['password2']
    
# Class ga assoslangan Sign up view uchun kengaytirilgan forma 
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Foydalanuvchi nomi')  
    first_name = forms.CharField(label='Ismingiz')
    last_name = forms.CharField(label='Familyangiz')
    email = forms.EmailField(label='Email manzilingiz')
    password1 = forms.CharField(label="Parolingiz", widget=forms.PasswordInput())
    password2 = forms.CharField(label='Parolni tasdiqlash', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class profileModelUpdateForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ['image', 'dateBirth']

class userModelUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']