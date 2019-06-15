from django.shortcuts import render, redirect
from .models import Match
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

# Create your views here.
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('matches_index')
    else:
      error_message = 'Invalid Credentials - Try Again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def matches_index(request):
  matches = Match.objects.all()
  return render(request, 'matches/index.html', {'matches': matches})

class MatchCreate(CreateView):
  model = Match
  fields = ['name', 'email', 'phone', 'age', 'location', 'meet', 'interests', 'zodiac', 'see_again', 'ghost']
  success_url = '/matches/'

  # def form_valid(self, form):
  # # Assign the logged in user
  #   form.instance.user = self.request.user
  #   # Let the CreateView do its job as usual
  #   return super().form_valid(form)

class MatchDetail(DetailView):
  model = Match

class UserDetail(DetailView):
  model = User
  