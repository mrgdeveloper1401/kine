from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ('create_at',)
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl', 'placeholder': 'enter title'}),
            'email': forms.EmailInput(attrs={'class': 'input input-bordered w-full rounded-xl', 'placeholder': 'enter email'}),
            'body': forms.Textarea(attrs={'class': "input input-bordered w-full rounded-xl"})
        }