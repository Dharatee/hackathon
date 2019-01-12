from typing import Dict, Any
from django.shortcuts import render, get_object_or_404, redirect
from user.models import User, Transaction, Card
from company.models import Company, Device
from datetime import datetime
import random


def index(request):
    if 'user' in request.session and 'acountType' in request.session == 'user':
        user = User.objects.get(name=request.session['user'])
        return render(request, 'user/index.html', {'user': user})
    elif 'user' in request.session and 'accountType' in request.session == 'company':
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
        accountType = request.POST['accountType']

        if accountType == 'user':
            name = request.POST['userName']
            password = request.POST['password']
            accountType = request.POST['accountType']
            user = User.objects.filter(name=name, password=password)
            if not user:
                err_msg = "Login Invalid"
                context = {'err_msg': err_msg}
                return render(request, 'main/index.html', context)
            user = User.objects.get(name=name, password=password)

            request.session['user'] = name
            request.session['accountType'] = accountType
            print(request.session['user'])
            print(request.session['accountType'])
            return render(request, 'user/index.html', {'user': user})
        else:
            name = request.POST['userName']
            password = request.POST['password']
            accountType = request.POST['accountType']
            user = Company.objects.filter(username=name, password=password)
            if not user:
                err_msg = "Login Invalid"
                context = {'err_msg': err_msg}
                return render(request, 'main/index.html', context)
            user = Company.objects.get(username=name, password=password)

            request.session['user'] = name
            request.session['accountType'] = accountType
            print(request.session['user'])
            print(request.session['accountType'])
            return render(request, 'company/index.html', {'user': user})