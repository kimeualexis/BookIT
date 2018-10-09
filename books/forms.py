from django import forms
from .models import Book
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('author', 'title', 'publisher', 'type', 'description', 'book', 'cover')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
