from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),
    path('cancel/', views.cancel),
]
