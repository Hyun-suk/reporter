from django import forms
from .models import Reporter


class NewReporterForm(forms.ModelForm):

    class Meta:
        model = Reporter
        fields = ['name', 'categories', 'affiliation']
        widgets = {
            'categories': forms.Select(),
        }
