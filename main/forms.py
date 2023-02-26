from django.forms import ModelForm
from .models import Item
from django import forms

class UserItem(ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Add...',
        'class': 'form-control'
        }), label='')
    class Meta:
        model = Item
        fields = ['text']
        
