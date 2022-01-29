from django import forms
from .models import Book


class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['borrower']
        widgets = {"borrower": forms.HiddenInput()}


class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['borrower']
        widgets = {"borrower": forms.HiddenInput()}
