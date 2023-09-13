from django import forms
from .models import Person
from django.core.exceptions import ValidationError


def validate_string(value):
    if not value.replace('', '').isalpha():
        raise ValidationError("Only strings values are allowed here.")


class PersonEditForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'bio')


class PersonInfoForm(forms.Form):
    first_name = forms.CharField(validators=[validate_string])
    last_name = forms.CharField(validators=[validate_string])
    email = forms.EmailField(required=False)
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'col': 2}))


class PersonDeleteForm(forms.Form):
    delete_my_profile = forms.BooleanField(required=False)


