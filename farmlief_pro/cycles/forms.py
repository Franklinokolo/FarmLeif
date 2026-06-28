from django import forms
from . models import Cycle


class cycleForm(forms.ModelForm):

    class Meta:
        model = Cycle
        fields = [
            'name',
            'cycle_type',
            'start_date',
            'end_date',
            'crop_type',
            'season',
            'livestock_type',
            'breed',
            'initial_count',

        ]

        widgets = {
            'name': forms.TextInput(attrs={ 'class' : 'form-control'}),
            'cycle_type' : forms.Select(attrs={'class' : 'form-select'}),
            'start_date' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}, format='%Y-%M-%d'),
            'end_date' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}, format='%Y-%M-%d'),
            'crop_type' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'eg vegetable, corn, tomatoe'}),
            'season' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'eg dry season'}),
            'livestock_type' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'eg poultry, goat, piggery, sheep'}),
            'breed' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'eg layers, broilers, cockerel'}),
            'initial_count' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }