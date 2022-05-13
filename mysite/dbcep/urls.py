from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('reservation/',views.reservation,name='reservation'),
    path('menu/',views.menu,name='menu'),
    path('gallery/',views.gallery,name='gallery'),
    path('core_body/',views.gallery,name='core_body'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup')
]