from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages

from django.shortcuts import render

from django.views.generic import (CreateView,ListView,UpdateView,DetailView,DeleteView)

from django.urls import reverse_lazy

from . models import Book



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
            return redirect('home') 
    


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
    success_url = reverse_lazy('book_list')
class BookCreateView(CreateView):
    pass