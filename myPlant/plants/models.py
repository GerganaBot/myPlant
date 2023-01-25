from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


PLANT_TYPES = [
    ('Outdoor Plants', 'Outdoor Plants'),
    ('Indoor Plants', 'Indoor Plants'),
]


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)], blank=False, null=False)
    first_name = models.CharField(max_length=20, validators=[RegexValidator('^[A-Z].*', 'Your name must start with a capital letter!')])
    last_name = models.CharField(max_length=20, validators=[RegexValidator('^[A-Z].*', 'Your name must start with a capital letter!')])
    profile_picture = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Plant(models.Model):
    plant_type = models.CharField(max_length=14, choices=PLANT_TYPES, null=False, blank=False)
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2), RegexValidator('[a-zA-Z]',
                                                                                             'Plant name should contain only letters!')])
    image_url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)

