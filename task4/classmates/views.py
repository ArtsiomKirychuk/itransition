from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import Message
from django.contrib.auth.decorators import login_required


def index(request):
    message, create = Message.objects.get_or_create()
    return render(request, 'classmates/home.html',{'message':message})

@login_required(login_url='/')
def addBro(request):
    add(request, True)
    return redirect('classmates:home')

@login_required(login_url='/')
def addSis(request):
    add(request, False)
    return redirect('classmates:home')

def add(request, brosis):
    message = Message.objects.first()
    message.title = 'Bro!' if brosis else 'Sis!'
    message.username = request.user.username
    if brosis: message.bro += 1
    else: message.sis += 1
    message.save()