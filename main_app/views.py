from django.shortcuts import render, redirect
from .models import Match

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def matches_index(request):
  matches = Match.objects.all()
  return render(request, 'index.html', {'matches': matches})