from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    #include django default auth urls.
    path('', include('django.contrib.auth.urls')),
]
