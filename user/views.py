from typing import Dict, Any
from django.shortcuts import render, redirect, get_object_or_404
from user.models import User, Transaction, Card
from company.models import Company, Device

def index(request):
    if 'user' in request.session and 'acountType' in request.session == 'user':
        user = User.objects.get(name=request.session['user'])
        return render(request, 'user/index.html', {'user': user})
    elif 'user' in request.session and 'acountType' in request.session == 'company':
        user = Company.objects.get(username=request.session['user'])
        return render(request, 'company/index.html', {'user': user})
    return redirect('main:index')



def logout(request):
    if 'user' in request.session:
        del request.session['user']
        del request.session['accountType']
    return redirect('main:index')