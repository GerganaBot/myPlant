from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)], blank=False, null=False)
    first_name = models.CharField(max_length=20, validators=[RegexValidator('^[A-Z].*', 'Your name must start with a capital letter!')])
    last_name = models.CharField(max_length=20, validators=[RegexValidator('^[A-Z].*', 'Your name must start with a capital letter!')])
    profile_picture = models.URLField(blank=True, null=True)

