from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required

def landing(request):
    return render(request, 'landingpage.html')
