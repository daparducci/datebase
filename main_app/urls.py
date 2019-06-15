from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('matches/', views.matches_index, name='matches_index'),
    path('matches/create', views.MatchCreate.as_view(), name="matches_create"),
    path('matches/<int:match_id>', views.MatchDetail.as_view(), name="match_detail"),
]