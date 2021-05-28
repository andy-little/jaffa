from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def setups(request):
    return render(request, 'main/setups.html')

def equipment(request):
    return render(request, 'main/equipment.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')

