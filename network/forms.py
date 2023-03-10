from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'location', 'website','dob']
        widgets = {
                    'bio': forms.TextInput(attrs={'class': 'profile_form', 'maxlength': 140}),
                    'location': forms.TextInput(attrs={'class': 'profile_form', 'maxlength':140}),
                    'website': forms.URLInput(attrs={'class': 'profile_form'}),
                    'dob': forms.DateInput(attrs={'class': 'profile_form' }),
                    }
