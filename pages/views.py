from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreatUserForm
from .models import Texts, Messages, Lessons
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import time

def index_view(request):
    return render(request, 'pages/index.html')

def onas_view(request):
    return render(request, 'pages/onas.html')

def actual_view(request):
    listoftexts = Texts.objects.order_by('-pub_date')
    context = {
        'listoftexts': listoftexts,
    }
    return render(request, 'pages/aktualnosci.html', context)

def kontakt_view(request):
    info_message = None
    context = {
    }
    if request.method == 'POST':
        if request.user.is_authenticated == True:
            user = User.objects.get(username=request.user.username)
            message = Messages()
            message.title = request.POST.get('title')
            message.user_email = request.POST.get('email')
            message.desc = request.POST.get('desc')
            message.pub_date = timezone.now()
            message.sender = user.username
            if message.title != "" and message.user_email != "" and message.desc != "":
                message.save()
                info_message = 'Wiadomość została wysłana.'
            else:
                info_message = 'Jedno lub więcej z powyższych pól nie jest wypełnione.'
        else:
            info_message = 'Błąd, nie jesteś zalogowany(a)!'
    context = {
        'info_message': info_message,
    }
    return render(request, 'pages/kontakt.html', context)

@login_required(login_url='../login')
def zajecia_view(request):
    listofLessons = Lessons.objects.order_by('-pub_date')
    context = {
        "listofLessons":listofLessons
    }
    return render(request, 'pages/zajecia.html', context)
def register_view(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            #return redirect('../login/')

    context = {
        'form': form,
    }
    if request.user.is_authenticated == True:
        allog = 'Jeteś już zalogowany!'
        context = {
            'form':form,
            'allog':allog
        }
    return render(request, 'pages/register.html', context)
def login_view(request):
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../')
            else:
                messages.info(request, 'Hasło Bądź login nie jest poprawne! ')
        return render(request, 'pages/login.html', context=None)
    else:
        return redirect('../register/')

@login_required(login_url='../../login')
def profile_view(request):
    username = None
    first_name = None
    email = None
    ps_ch = False
    if request.user.is_authenticated == True:
        username = request.user.username
        first_name = request.user.first_name
        email = request.user.email
        sucess = ''
    context = {
        'username': username,
        'first_name': first_name,
        'email': email,
        'sucess': sucess,
    }
    if request.method == 'POST':
        user = User.objects.get(username=username)
        if request.POST.get('first_name') != '':
            user.first_name = request.POST.get('first_name')
            sucess += 'Imię, '
        if request.POST.get('password') != '':
            user.set_password(request.POST.get('password'))
            sucess += 'Hasło, '
            ps_ch = True
        if request.POST.get('email') != '':
            user.email = request.POST.get('email')
            sucess += 'E-mail '
        if sucess != '':
            sucess += 'Zmiany zostały zapisane'
        user.save()
        context = {
            'username': username,
            'first_name': first_name,
            'email': email,
            'sucess': sucess,
        }
    if ps_ch == True:
        return redirect('../../login')
    return render(request, 'pages/profile.html', context)
def logout_view(request):
    logout(request)
    return redirect('../login')
