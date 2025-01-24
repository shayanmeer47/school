from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('edit-message/<int:id>', views.editContact, name='edit-contact'),
    path('delete-message/<int:id>', views.deleteContact, name='delete-contact'),
    path('gallery', views.gallery, name='gallery'),
]