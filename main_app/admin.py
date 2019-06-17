from django.contrib import admin
from .models import Match, Rdv, Match_photo, User_photo
# Register your models here.
admin.site.register(Match)
admin.site.register(Rdv)
admin.site.register(Match_photo)
admin.site.register(User_photo)