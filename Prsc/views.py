from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *


def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def apply_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        p=Player()
        p.name = name
        p.phone = phone
        p.email = email

        p.save()

        print(name)
        print(phone)
        print(email)

        messages.success(request, 'Application submitted successfully!')
        return redirect('/')

    return render(request, 'apply.html')

def members_show(request):
    plyr = Player.objects.all()
    return render(request, 'members.html',{"player":plyr})