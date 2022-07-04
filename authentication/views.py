from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import CustomUser
from django.contrib.auth import authenticate, login


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
            return render(request, "authentication/home.html", {'fname':fname})
            

        else:
            messages.error(request, "Invalid input")
            return redirect('home') 
    


    return render(request, "authentication/signin.html")


def signout(request):
    pass
