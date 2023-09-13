from django import forms
from .models import Person


class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'bio')


class PersonDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(required=False)


class PersonEditForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'bio')

