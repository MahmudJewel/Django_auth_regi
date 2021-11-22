from django.urls import path, include
from second import views

urlpatterns = [
    path('',views.home, name='home'),
]
