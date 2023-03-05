from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'dob', 'location', 'website']
        widgets = {
                    'bio': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 280}),
                    'dob': forms.Textarea(attrs={'rows':2, 'class': 'form-control' }),
                    'location': forms.DateField(attrs={'class': 'form-control', 'maxlength':140}),
                    'website': forms.URLField(attrs={'class': 'form-control'}),
                    }
