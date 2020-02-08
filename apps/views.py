from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.contrib.sessions.models import Session

# Create your views here.
def index(req):
    users = User.objects.all()
    # se = req.session['id']
    # cur = User.objects.get(id = se)
    context = {
        'users': users,
        # 'curent':cur,
    }
    return render(req,"index.html",context)

def success(req):
    return render(req,"success.html")

def login(req):
    return render(req,"login.html")

def regist(req):
    return render(req,"regist.html")

def create_user(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        print(errors)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/regist')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            location = request.POST['location']
            password = request.POST['password']
            phone = request.POST['phone_number']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(phone_number = phone ,on_call = False, first_name = first_name,last_name = last_name, email = email,location = location, password = pw_hash)
            return redirect('/success')

def user_login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        else: 
            user = User.objects.get(email = request.POST['email'])
            request.session['id'] = user.id
            return redirect('/')

    
def show(req,id):
    user = User.objects.get(id = id)
    context = {'user' : user}
    return render(req,'show.html',context)


def jobs(req):
    jobs = Jobs.objects.all()
    context = {
        'jobs' : jobs
    }
    return render(req,'jobs.html',context)
