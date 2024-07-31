from django.urls import path
from . import views 

urlpatterns = [
    path('', views.registration ,name ='registration'),
    path('registration', views.registration ,name ='registration'),
    path('login', views.login, name='login'),
    path('index', views.index ,name ='index'),
    path('index1', views.index, name='index')
]