from django.shortcuts import render
from . models import Book

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'loans/home.html', {})

def list_books(request):
    data = {}
    data['books'] = Book.objects.all()
    return render(request, 'loans/list.html', data)
    