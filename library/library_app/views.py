from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BorrowBookForm, ReturnBookForm

books_list = [
    {'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    {'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    {'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency',
        'author': 'Alexander McCall Smith'}
]


def home(request):
    return render(request, "home.html")


def books(request):
    data = {"books": Book.objects.all()}
    return render(request, "books.html", data)


@login_required
def show(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == "POST":
        if "borrow_book" in request.POST:
            borrow_form = BorrowBookForm(request.POST)
            return_form = ReturnBookForm()
            if borrow_form.is_valid():
                book.borrower = request.user
                book.save()
                return redirect("library-book", id=id)
        elif "return_book" in request.POST:
            return_form = ReturnBookForm(request.POST)
            borrow_form = BorrowBookForm()
            if return_form.is_valid():
                book.borrower = None
                book.save()
                return redirect("library-book", id=id)
    else:
        borrow_form = BorrowBookForm()
        return_form = ReturnBookForm()
    data = {"book": book, "borrow_form": borrow_form,
            "return_form": return_form}
    return render(request, "book.html", data)


def not_found_404(request, exception):
    data = {"err": exception}
    return render(request, "404.html", data)
