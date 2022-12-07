"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
	
    class Meta:
        model = Thing
        fields=["name","description","quantity"]

    name=forms.CharField(
        label="name",
    )

    description=forms.CharField(
        label="description",
        widget = forms.Textarea(),
    )

    quantity=forms.IntegerField(
        widget = forms.NumberInput(),
        label="quantity",
    )


