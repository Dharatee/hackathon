from typing import Dict, Any
from django.shortcuts import render, redirect, get_object_or_404
from user.models import User, Transaction, Card
from company.models import Company, Device

def index(request):
    if request.session['user'] == '':
        return redirect('main:index')
    elif request.session['user'] != '' and request.session['accountType'] == 'company':
        user = Company.objects.get(username=request.session['user'])
        return render(request, 'company/index.html', {'user': user})
    user = User.objects.get(name=request.session['user'])
    return render(request, 'user/index.html', {'user': user})

def logout(request):
    request.session['user']=""
    request.session['accountType']=""
    return redirect('main:index')