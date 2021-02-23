from django.contrib import admin
from payment.models import StripeCustomer


admin.site.register(StripeCustomer)
