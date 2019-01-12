from typing import Dict, Any
from django.shortcuts import render, get_object_or_404, redirect
from user.models import User
from company.models import Company
from datetime import datetime
import random

def index(request):
    return render(request, 'main/index.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        address = request.POST["address"]
        bloodGroup = request.POST["bloodGroup"]
        userType = request.POST["userType"]
        password = request.POST["password1"]

        data = User()
        data.name = name
        data.email = email
        data.contact = contact
        data.address = address
        data.card_key = '%4x' % random.getrandbits(4*4) + '-' + '%4x' % random.getrandbits(4*4) + '-' + '%4x' % random.getrandbits(4*4) + '-' + '%4x' % random.getrandbits(4*4)
        data.blood_group = bloodGroup
        data.user_type = userType
        data.password = password
        data.register_date = datetime.now()
        data.save()

    return render(request, 'main/index.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['userName']
        password = request.POST['password']
        accountType = request.POST['accountType']

        if accountType == 'user':
            data = User.objects.filter(name=name, password=password)
            request.session['user'] = name
            request.session['accountType'] = accountType
            # request.session['id'] = data.id
            return render(request, 'user/index.html')
        else:
            data = Company.objects.filter(username=name, password=password)
            request.session['user'] = name
            request.session['accountType'] = accountType
            # request.session['id'] = data.id
            return render(request, 'company/index.html')
