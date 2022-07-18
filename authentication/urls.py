from django.urls import path 
from . import views
from django.urls import path
from .views import BookListView, BookDetailView, BookUpdateView, BookDeleteView, BookCreateView


app_name = 'authentication'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"), 
    path('signout', views.signout, name="signout"),
    path('booklist/', BookListView.as_view(), name="book_list"),
    path('create/', BookCreateView.as_view(), name="book_create"),
    path('<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('<int:pk>/update/', BookUpdateView.as_view(), name="book_update"),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name="book_delete"),
    path('index', views.index, name='index'),

]
   