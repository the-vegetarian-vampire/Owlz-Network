from django import forms

from .models import User, Comment

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

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['new_comment']
        widgets = {
                    'new_comment': forms.TextInput(attrs={'class': '', 'maxlength': 440}),
                    }
