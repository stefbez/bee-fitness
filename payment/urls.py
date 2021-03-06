from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('config/', views.stripe_config),
    path(
        'create-checkout-session/',
        views.create_checkout_session,
        name='create-checkout-session'
        ),
    path('success/', views.success),
    path('cancel/', views.cancel),
    path('webhook/', views.stripe_webhook),
    path('check-paid-status/', views.check_paid_status),
]
