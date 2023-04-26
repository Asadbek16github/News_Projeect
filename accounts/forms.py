from django.contrib.auth.models import User
from django import forms

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