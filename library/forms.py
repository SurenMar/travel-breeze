from django import forms

class CityForm(forms.Form):
    city = forms.CharField(
        max_length=50,
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'City',
        })
    )
    
class CountryForm(forms.Form):
    country = forms.CharField(
        max_length=50,
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Country',
        })
    )