from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ['photo', 'year']