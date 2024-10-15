# book/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'rating']
        labels = {
            'title': 'Título:',
            'author': 'Autor:',
            'rating': 'Valoración:'
        }
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 10000}),
        }