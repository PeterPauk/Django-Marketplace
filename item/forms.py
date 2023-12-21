from django import forms
from .models import Item

class NewItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = {'category', 'name', 'description', 'price', 'image',}

class EditItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = {'name', 'description', 'price', 'image', 'is_sold'}
