from django.shortcuts import render, redirect
from .models import Match
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
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
  