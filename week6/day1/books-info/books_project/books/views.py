import json
from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, BookReview, BookForm


def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)


def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    context = {'book': book}
    return render(request, 'book_detail.html', context)

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect to the list of books after saving
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'create_book.html', context)