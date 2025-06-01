from django import forms

class CityForm(forms.Form):
    city = forms.CharField(
        max_length=50,
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'City',
            'id': 'city-search-box',
        })
    )
    
class CountryForm(forms.Form):
    country = forms.CharField(
        max_length=50,
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Country',
            'id': 'country-search-box',
        })
    )