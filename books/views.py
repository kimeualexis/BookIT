from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from . models import Book
from . forms import BookForm, UserForm


@login_required(login_url='books:login_user')
def index(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/index.html', {'books': books})


@login_required(login_url='books:login_user')
def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/details.html', {'book': book})


def delete(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return render(request, 'books/index.html', {'book': book})


@login_required(login_url='books:login_user')
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.cover = request.FILES['cover']
            book.save()
            return render(request, 'books/details.html', {'book': book})
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.filter(user=request.user)
                return render(request, 'books/index.html', {'books': books})
    context = {'form': form, }
    return render(request, 'books/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.filter(user=request.user)
                return render(request, 'books/index.html', {'books': books})
            else:
                return render(request, 'books/login.html', {'error_message': 'Your Account is Disabled!'})
        else:
            return render(request, 'books/login.html', {'error_message': 'Invalid Login!'})
    return render(request, 'books/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'books/login.html', {'form': form})


def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book.html', {'book': book})


def favorite(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    try:
        if book.is_favorite:
            book.is_favorite = False
        else:
            book.is_favorite = True
        book.save()
    except(KeyError, Book.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def favorites(request):
    user = request.user
    books = Book.objects.filter(is_favorite=True)
    return render(request, 'books/favorites.html', {'books': books, 'user': user})

