from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('',views.home,name='home'),
    path('chat/',views.chat,name='chat'),
    path('getResponse',views.getResponse,name='getResponse'),
    path('appointment',views.appointment,name='appointment'),

]