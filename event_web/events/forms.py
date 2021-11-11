from django import forms
from django.forms import ModelForm
from .models import Venue

#create a Venue form
class VenueForm(ModelForm):
    class Meta:
        model= Venue
        fields = ('name','address','zip_code','phone_number','email_address')
        