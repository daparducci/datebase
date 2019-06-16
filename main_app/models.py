from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField


# Create your models here. Don't forget to register them in admin.py (admin.site.register(modelname))

class Match(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(
        max_length=100,
        blank = True
    )
    phone = models.CharField(max_length=100, blank = True)
    age = models.IntegerField(null= True)
    location = models.TextField(blank = True)
    meet = models.TextField()
    interests = models.TextField(blank = True)
    # attraction = models.IntegerField(
    #     # choices=(
    #     #     (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
    #     # ),
    #     blank = True
    # )
    zodiac = models.CharField(
        max_length=100,
        choices=(
            ('Aries', 'Aries'), ('Taurus', 'Taurus'), ('Gemini', 'Gemini'),
            ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'),
            ('Scorpio', 'Scorpio'), ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'),
            ('Aquarius', 'Aquarius'), ('Pisces','Pisces')
        ),
        blank = True
    )
    see_again = models.BooleanField(null = True)
    ghost = models.BooleanField(null = True)

    def __str__(self):
        return self.name

class Rdv(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    date = models.DateField()
    what = models.TextField(blank=True)
    where = models.TextField(blank=True)
    # rating = models.IntegerField(
        # choices=(
        #     (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
        # ),
        # blank = True
    # )
    cancel = models.BooleanField(null=True)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.what 