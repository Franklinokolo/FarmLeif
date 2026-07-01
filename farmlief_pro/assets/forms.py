from django import forms
from .models import Asset




class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        field = [
            'name',
            'asset_type',
            'purchase value',
            'purchase date'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_type': forms.TextInput(attrs={'class' : 'form-control'}),
            'purchase_value' : forms.TextInput(attrs={'class' : 'form-control'}),
            'purchase date' : forms.TextInput(attrs={'class' : 'form-control'})
        }