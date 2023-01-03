from django.shortcuts import redirect, render
from . models import Book, Loan
from . form import BookForm, LoanForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'loans/home.html', {})

def list_books(request):
    data = {}
    data['books'] = Book.objects.all()
    return render(request, 'loans/list.html', data)

def new_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_list') 
    return render(request, 'loans/form_item.html', {'form': form})

@login_required(login_url="/login")
def new_loan(request, cod):
    book = Book.objects.get(cod = cod)

    if book.is_borrowed:
        return HttpResponse('Book already lent')

    form = LoanForm()
    
    return render(request, 'loans/form_loan.html', {'form': form, 'book': book })

def resolve_loan(request):
    form = LoanForm(request.POST)

    if form.is_valid():
        form.save()
        
    return HttpResponse('Erro interno do sistema')

def signup( request):
    if request.method == 'GET':
        return render(request, 'loans/signup.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password =request.POST.get('password')
        
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Already exists a user with this username')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('url_home')        

def login( request):
    if request.method == 'GET':
        return render(request, 'loans/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            django_login(request, user)
            return redirect('url_home')
        else:
            return render(request, 'loans/login.html')