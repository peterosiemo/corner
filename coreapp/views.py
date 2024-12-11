from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def events(request):
    return render(request, 'events.html')

def chefs(request):
    return render(request, 'chefs.html')

def gallery(request):
    return render(request, 'gallery.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def book(request):
    return render(request, 'book.html')
