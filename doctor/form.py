from django import forms
from .models import Doctor, QuestionDoctor


class SignUpDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            'medical_system_code',
            'nation_code',
            'address_doctor',
            'image',
            'doctor_birth_dat'
        )
        
        widgets = {
            'medical_system_code': forms.NumberInput(attrs={'class': 'input input-bordered my-2'}),
            'nation_code': forms.NumberInput(attrs={'class': 'input input-bordered  my-2'}),
            'address_doctor': forms.Textarea(attrs={'class': 'input input-bordered  my-2'}),
            'image': forms.FileInput(),
            'doctor_birth_dat': forms.DateInput(attrs={'class': 'input input-bordered my-2'}),
        }


class QuestionDoctorForm(forms.ModelForm):
    class Meta:
        model = QuestionDoctor
        fields = ('first_name', 'last_name', 'title', 'body')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'last_name': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'title': forms.TextInput(attrs={'class': 'input input-bordered w-full rounded-xl'}),
            'body': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full h-24 rounded-xl'})
        }
