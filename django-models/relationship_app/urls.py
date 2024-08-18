# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='home'),
    path('', views.LibraryDetails_view, name='home')
]