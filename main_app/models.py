from django.db import models
from django.urls import reverse
from datetime import date, time
import datetime
# Import the User
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField


# Create your models here. Don't forget to register them in admin.py (admin.site.register(modelname))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(
        max_length=100,
        choices=(
            ('M', 'Male'),
            ('F', 'Female'),
            ('N', 'Non-Binary'),
        ),
        blank = True
    )
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
    apps_used = models.CharField(
        max_length=100,
        choices=(
            ('Bumble', 'Bumble'),
            ('CoffeeMeetsBagel', 'CoffeeMeetsBagel'),
            ('Grindr', 'Grindr' ),
            ('Match', 'Match'),
            ('OkCupid', 'OkCupid'),
            ('POF', 'POF'),
            ('Hinge', 'Hinge'),
            ('Tinder', 'Tinder'),

        ),
        blank = True
    )
    relationship_goal = models.CharField(
        max_length=100,
        choices=(
            ('Relationship', 'Relationship'),
            ('Something Casual', 'Something Casual'),
            ('Not Sure', 'Not Sure'),
            ('Marriage', 'Marriage'),
        ),
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)



    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.id})

class Match(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(
        max_length=100,
        blank = True
    )
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.IntegerField(null= True)
    location = models.TextField(blank = True)
    meet = models.TextField()
    interests = models.TextField(blank = True)
    attraction = models.CharField(
        max_length=100,
        choices=(
            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')
        ),
        blank = True
    )
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

    def get_absolute_url(self):
        return reverse('match_detail', kwargs={'pk': self.id})
        
    def __str__(self):
        return self.name

class Rdv(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    date = models.DateField()
    rdv_time = models.CharField(max_length=10)
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
    
    def get_absolute_url(self):
        return reverse('rdv_detail', kwargs={'pk': self.id})

class Match_photo(models.Model):
    url = models.CharField(max_length=200)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for match_id:  {self.match_id} @{self.url}"

class User_photo(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for match_id:  {self.user_id} @{self.url}"