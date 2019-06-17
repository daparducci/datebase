from django.shortcuts import render, redirect
from .models import Match, Rdv, Match_photo, User_photo
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'datebase'

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

def add_match_photo(request, match_id):
  print(match_id)
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    session = boto3.Session(profile_name="datebase")
    s3 = session.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Match_photo(url=url, match_id=match_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('match_detail', pk=match_id)

def add_profile_photo(request, profile_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    session = boto3.Session(profile_name="datebase")
    s3 = session.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = User_photo(url=url, user_id=profile_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('profile', pk=profile_id)


def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def matches_index(request):
  matches = Match.objects.all()
  return render(request, 'matches/index.html', {'matches': matches})

class MatchCreate(CreateView):
  model = Match
  fields = ['name', 'email', 'phone', 'age', 'location', 'meet', 'interests', 'zodiac']
  success_url = '/matches/'

  def form_valid(self, form):
  # Assign the logged in user
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class MatchDetail(DetailView):
  model = Match

class MatchDelete(DeleteView):
  model = Match
  success_url = '/matches/'

class RdvCreate(CreateView):
  model = Rdv
  fields = ['match', 'date', 'what', 'where']
  success_url = '/rdvs/'

  # def form_valid(self, form):
  # # Assign the logged in user
  #   form.instance.user = self.request.user
  #   # Let the CreateView do its job as usual
  #   return super().form_valid(form)

class RdvList(ListView):
  model = Rdv

class RdvDetail(DetailView):
  model = Rdv

class RdvDelete(DeleteView):
  model = Rdv
  success_url= '/rdvs/'

class UserDetail(DetailView):
  model = User
  