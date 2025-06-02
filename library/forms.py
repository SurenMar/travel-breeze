from django import forms

class CityForm(forms.Form):
    """
    A form that lets user type in desired city in explore page
    """
    city = forms.CharField(
        max_length=50,
        required=True,
        label='City',
        widget=forms.TextInput(attrs={
            'placeholder': 'City',
            'id': 'city-search-box',
        })
    )
    
class CountryForm(forms.Form):
    """
    A form that lets user type in desired country in explore page
    """
    country = forms.CharField(
        max_length=50,
        required=True,
        label='Country',
        widget=forms.TextInput(attrs={
            'placeholder': 'Country',
            'id': 'country-search-box',
        })
    )