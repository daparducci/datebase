from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name="signup"),
    path('profile/<int:pk>', views.UserDetail.as_view(), name="profile"),

    path('matches/', views.matches_index, name='matches_index'),
    path('matches/create', views.MatchCreate.as_view(), name="matches_create"),
    path('matches/<int:pk>', views.MatchDetail.as_view(), name="match_detail"),

    path('rdvs/', views.RdvList.as_view(), name='rdvs_index'),
    path('rdvs/create', views.RdvCreate.as_view(), name="rdvs_create"),
    path('rdvs/<int:pk>', views.RdvDetail.as_view(), name="rdv_detail"),
]