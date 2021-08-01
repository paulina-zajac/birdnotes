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
        fields = ('species', 'appearance','number','gender','behaviour', 'place', 'time', 'weather' , 'description', 'photo')

        labels = {
            'species': 'species',
            'appearance' : 'appearance',
            'gender': 'gender',
            'behaviour': 'behaviour',
            'place' : 'where',
            'time': 'when',
            'number': 'number of birds',
            'weather': 'weather',
            'description': 'detailed description',
            'photo': 'photo',
        }

        species = forms.ModelChoiceField(queryset=BirdSpecies.objects.all())

        widgets = {
            'species': forms.Select(attrs={'class': 'form-control'}),
            'appearance': forms.Textarea(attrs={'class': 'form-control','placeholder':'appearance', 'style': 'height:200px;'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'number'}),
            'behaviour': forms.Textarea(attrs={'class': 'form-control',  'placeholder': 'behaviour'}),
            'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'place'}),
            'time': forms.DateTimeInput(attrs={'class': 'form-control','placeholder':'time'}),
            'weather': forms.TextInput(attrs={'class': 'form-control','placeholder':'weather'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'description', 'style': 'height:200px;'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'photo'}),

        }
