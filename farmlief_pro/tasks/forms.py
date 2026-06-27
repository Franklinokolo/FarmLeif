from django import forms
from . models import Task


class taskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"},
            format="%Y-%m-%d"
        ),
        input_formats=["%Y-%m-%d"]
    )
    time = forms.TimeField(
        widget= forms.TimeInput(
            attrs={"class" : "form-control", "type" : "time"},
            format= "%h-%m%"
        )
    )
    class Meta:
        model = Task
        fields = [
            'title',
            'type',
            'priority',
            'time',
            'due_date',
            'description',
            'Cycle'

        ]

        widgets = {
            "title" : forms.TextInput(attrs={'class' : 'form-control'}),
            'type' : forms.Select(attrs={'class' : 'form-select'}),
            'priority' : forms.Select(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'Cycle' : forms.Select(attrs={'class' : 'form-select'})
        }
    