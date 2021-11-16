from django import forms
from django.forms import ModelForm
from .models import Venue

#create a Venue form
class VenueForm(ModelForm):
    class Meta:
        model= Venue
        fields = ('name','address','zip_code','phone_number','email_address','website')

        labels = {
            'name':'',
            'address':'',
            'zip_code':'',
            'phone_number':'',
            'email_address':'',
            'website':'',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Venue Name'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'zip code'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'contact'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'website':forms.TextInput(attrs={'class':'form-control','placeholder':'website link'}),
        }