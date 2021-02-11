from django.shortcuts import render


def payment(request):
    """ A view to return the index page """
    return render(request, 'payment/payment.html')
