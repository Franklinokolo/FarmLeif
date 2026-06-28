from django import forms
from .models import Enterprise


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields =[
            'name',
            'location',
            'farm_type',
            'farmer'
        ] 
    

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'location' : forms.TextInput(attrs={'class': 'form-control'}),
            'farm_type' : forms.Select(attrs={'class' : 'form-select'}),
            'farmer' : forms.TextInput(attrs={'class' : 'form-control', 'readonly' : 'readonly'})
        }

    def __init__(self, *args, **kwargs):
        # Extract the user passed from the view
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            # Safely set the initial text value to the username
            self.fields['farmer'].initial = user.username
            
        # Lock the field securely using readonly so it still submits data
        self.fields['farmer'].widget.attrs['placeholder'] = user.username