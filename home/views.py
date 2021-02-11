from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """
    return render(request, 'home/about.html')


def gym(request):
    """ A view to return the gym page """
    return render(request, 'home/gym.html')


def racquets(request):
    """ A view to return the racquets page """
    return render(request, 'home/racquets.html')


def swim(request):
    """ A view to return the swim & spa page """
    return render(request, 'home/swim.html')
