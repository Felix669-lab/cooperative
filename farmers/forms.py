from django import forms
from .models import Farmer

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ID number'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'county': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter county'}),
            'sub_county': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter sub-county'}),
            'ward': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ward'}),
            'farm_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter farm name'}),
            'animal_type': forms.Select(attrs={'class': 'form-control'}),
            'number_of_animals': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of animals'}),
            'animal_age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age in months'}),
        }