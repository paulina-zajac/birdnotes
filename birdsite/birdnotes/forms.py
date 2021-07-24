from .models import Observation, BirdSpecies
from django import forms


class ObservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    def clean_number(self):
        number = self.cleaned_data['number']
        if number <= 0:
            raise forms.ValidationError('Minimum number of birds is 1')
        return number

    class Meta:
        model = Observation
        fields = ('species', 'appearance', 'place', 'time', 'number', 'description')

        labels = {
            'species': 'species',
            'appearance' : 'appearance',
            'place' : 'where',
            'time': 'when',
            'number': 'number of birds',
            'description': 'detailed description'
        }

        species = forms.ModelChoiceField(queryset=BirdSpecies.objects.all())

        widgets = {
            'species': forms.Select(attrs={'class': 'form-control'}),
            'appearance': forms.Textarea(attrs={'class': 'form-control','placeholder':'x', 'style': 'height:200px;'}),
            'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'x'}),
            'time': forms.DateTimeInput(attrs={'class': 'form-control','placeholder':'x'}),
            'number': forms.NumberInput(attrs={'class': 'form-control','placeholder':'x'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'x', 'style': 'height:200px;'})
        }

