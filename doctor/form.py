from django import forms
from .models import Doctor


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
            'medical_system_code': forms.NumberInput(attrs={'class': 'input input-bordered w-full my-2'}),
            'nation_code': forms.NumberInput(attrs={'class': 'input input-bordered w-full my-2'}),
            'address_doctor': forms.Textarea(attrs={'class': 'input input-bordered w-full my-2'}),
            'image': forms.FileInput(),
            'doctor_birth_dat': forms.DateInput(attrs={'class': 'input input-bordered w-full my-2'}),
        }