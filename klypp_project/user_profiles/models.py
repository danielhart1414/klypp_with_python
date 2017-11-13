from django.db import models
from django.core.validators import RegexValidator


# This class captures essential user information for the signup form.
class KlyppUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$',
                                 message="Phone number must be entered in the format: '9999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list
    password = models.CharField(max_length=100)
    PROFILE_CHOICES = [("Stylist", "Stylist"), ("Client", "Client"), ("Both", "Both")]
    profile_type = models.CharField(max_length=7, choices=PROFILE_CHOICES, default='Stylist')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + " - " + self.profile_type
