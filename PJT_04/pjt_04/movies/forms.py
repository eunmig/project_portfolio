from django import forms
from django.forms import widgets
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(
            attrs={
            }
        ),
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(
            attrs={
                'rows': 8,
                'cols': 40,

            }
        )
    )
    
    class Meta:
        model = Movie
        fields = '__all__'


