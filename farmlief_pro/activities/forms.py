from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    activity_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"},
            format="%Y-%m-%d"
        ),
        input_formats=["%Y-%m-%d"]
    )

    class Meta:
        model = Activity
        fields = [
            "title",
            "description",
            "activity_type",
            "quantity",
            "unit",
            "cost",
            "activity_date",
        ]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "activity_type": forms.Select(attrs={"class": "form-select"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "unit": forms.TextInput(attrs={"class": "form-control"}),
            "cost": forms.NumberInput(attrs={"class": "form-control"}),
        }