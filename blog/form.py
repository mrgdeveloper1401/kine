from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Comment


class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'body',
        )
        
        widgets = {
            'body': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full h-36 rounded-3xl', 'placeholder': 'لطفا نظر خود را وارد کنید'}),
        }
        
        error_messages = {
            'required': _( 'لطفا این فیلد ها  رو پر کنید'),
        }
        
        labels = {
            'body': _('متن نظر')
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'body',
        )