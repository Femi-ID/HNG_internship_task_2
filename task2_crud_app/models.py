from django.db import models
from django.core.exceptions import ValidationError


# custom validator to accept only string values
def validate_string(value):
    if not isinstance(value, str):
        raise ValidationError("Only strings values are allowed here.")


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField(blank=True, max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Full name: {self.first_name} {self.last_name}'

