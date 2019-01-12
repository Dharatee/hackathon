from typing import Dict, Any
from django.shortcuts import render, get_object_or_404, redirect
from user.models import User, Transaction, Card
from company.models import Company, Device
from datetime import datetime
import random


def index(request):
    if request.session['user'] != ''  and request.session['accountType'] == 'user':
        user = User.objects.get(name=request.session['user'])
        return render(request, 'user/index.html', {'user': user})
    elif request.session['user'] != '' and request.session['accountType'] == 'company':
        user = Company.objects.get(username=request.session['user'])
        return render(request, 'company/index.html', {'user': user})
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
            user = User.objects.filter(name=name, password=password)
            if not user:
                err_msg = "Login Invalid"
                context = {'err_msg': err_msg}
                return render(request, 'main/index.html', context)
            user = User.objects.get(name=name, password=password)
            request.session['user'] = name
            request.session['accountType'] = accountType
            request.session['id'] = user.id
            return render(request, 'user/index.html', {'user': user})
        else:
            user = Company.objects.filter(username=name, password=password)
            if not user:
                err_msg = "Login Invalid"
                context = {'err_msg': err_msg}
                return render(request, 'main/index.html', context)
            user = Company.objects.get(username=name, password=password)
            request.session['user'] = name
            request.session['accountType'] = accountType
            request.session['id'] = user.id
            return render(request, 'company/index.html', {'user': user})