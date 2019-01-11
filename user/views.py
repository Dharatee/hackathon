from typing import Dict, Any
from django.shortcuts import render, get_object_or_404
from .models import User, Transaction, Card

def index(request):
    return render(request, 'user/index.html')
