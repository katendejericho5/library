from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from elibrary import settings
from django.shortcuts import render

from django.views.generic import (CreateView,ListView,UpdateView,DetailView,DeleteView)

from django.urls import reverse_lazy

from . models import Book



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
        '''

        subject ='Welcome to elibrary'
        message ='Hi ,thank you for registering in library'
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[user.email,]
        send_mail(subject,message,email_from,recipient_list)'''



    return render(request, "authentication/signup.html")

  


def signin(request):
    books = Book.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "books/book_list.html", {'books':books})
            

        else:
            messages.error(request, "Invalid input")
            return redirect('/') 
    


    return render(request, "authentication/signin.html")


def signout(request):
    pass

# Create your views here.

class BookListView(ListView):
    model=Book
    template_name="books/book_list.html"
    context_object_name="books"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "books"

class BookUpdateView(UpdateView):
    model = Book
    fields = ('title', 'user', 'status',)
    template_name = "books/book_update.html"


class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy('authentication:book_list')
class BookCreateView(CreateView):
    pass
def index(request):
    return render(request, "authentication/index.html")

def  signout(request):
    messages.success(request, "Logged out successfully!")
    return redirect('/')
def message(request):
        return render(request, "books/message.html")

def credit(request):
        return render(request, "books/credit.html")

from django.core.mail import send_mail
from django.conf import settings
#send_mail(
#subject='A cool subject',
      #message='A stunning message',
      #from_email=settings.EMAIL_HOST_USER,
      #recipient_list=[settings.RECIPIENT_ADDRESS])
#1
def search(request):
    if request.method != 'POST':
        return render(request, "books/book_list.html")
    else:
        searched = request.POST['search']
        try:
            book = Book.objects.get(title__contains=searched)
        except Book.DoesNotExist:
            book = None
            return render(request, 'authentication/search.html', {'book': book})
        else:
            return render(request, 'authentication/search.html', {'book': book})



from django.conf import settings
from django.core.mail import send_mail
