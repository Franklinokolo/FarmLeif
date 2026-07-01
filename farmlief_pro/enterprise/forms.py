from django import forms
from .models import Enterprise

class EnterpriseForm(forms.ModelForm):
    # 1. Create a dummy display-only field for the visual layout
    farmer_display = forms.CharField(
        label="Farmer",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'})
    )

    class Meta:
        model = Enterprise
        fields = ['name', 'location', 'farm_type', 'farmer'] 
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'farm_type': forms.Select(attrs={'class': 'form-select'}),
            # 2. Turn the real farmer field into a hidden input so the ID transmits cleanly
            'farmer': forms.HiddenInput() 
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            # 3. Put the readable name into the disabled visual field
            self.fields['farmer_display'].initial = user.username
            
            # 4. Put the required database primary key ID into the hidden validation field
            self.fields['farmer'].initial = user.id
            
            # 5. Order the fields nicely so the display field shows up where you want it
            self.order_fields(['name', 'location', 'farm_type', 'farmer_display', 'farmer'])
