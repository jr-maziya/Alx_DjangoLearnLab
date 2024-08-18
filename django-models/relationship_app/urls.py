# myapp/urls.py
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('', views.book_list_view, name='home'),
    path('', views.LibraryDetails_view, name='home'),
    path(views.register", "LogoutView.as_view template_name=", "LoginView.as_view template_name=")
]