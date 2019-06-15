from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here. Don't forget to register them in admin.py (admin.site.register(modelname))

class Match(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = PhoneNumberField()
    age = models.IntegerField()
    location = models.TextField()
    meet = models.TextField()
    interests = models.TextField()
    attraction = models.IntegerField(
        choices=(
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
        )
    )
    zodiac = models.CharField(
        max_length=100,
        choices=(
            ('Aries', 'Aries'), ('Taurus', 'Taurus'), ('Gemini', 'Gemini'),
            ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'),
            ('Scorpio', 'Scorpio'), ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'),
            ('Aquarius', 'Aquarius'), ('Pisces','Pisces')
        ),
    )
    see_again = models.BooleanField()
    ghost = models.BooleanField()

    def __str__(self):
        return self.name
