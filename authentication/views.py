from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from elibrary import settings

from .models import CustomUser
from django.contrib.auth import authenticate, login, logout


User = get_user_model()
def home(request):
    return render(request, 'authentication/home.html')

def signup(request):


    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        snum = request.POST['snum']

        if User.objects.filter(username = username):
            messages.error(request, "Username already exists, try another username.")
            return redirect('home')

        if User.objects.filter(email = email).exists():
            messages.error(request, "Email already registered")
            return redirect('home')

        if len(username)>15:
            messages.error(request, "Username should not be greater than 15 characters")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")

        if not username.isalnum():
            messages.error(request, "username should consist of alpha-numeric characters")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.student_number = snum


        myuser.save()

        messages.success(request, "Your request has been created succesfully")

        return redirect('/signin')



    return render(request, "authentication/signup.html")

  


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname':fname})
            

        else:
            messages.error(request, "Invalid input")
            return redirect('/index') 
    


    return render(request, "authentication/signin.html")



def index(request):
    return render(request, "authentication/index.html")

def  signout(request):
    messages.success(request, "Logged out successfully!")
    return redirect('/')
