from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('gym/', views.gym, name='gym'),
    path('racquets/', views.racquets, name='racquets'),
    path('swim-spa/', views.swim, name='swim'),
]
