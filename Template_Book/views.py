from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):

    return render(request, "index.html")

def index_book(request ):

    some_data = Books.objects.all()

    context ={
        "contex":some_data
    }

    return render(request, "index_book.html", context)


def create_Book(request):
    errors = {}
    if len(request.POST['title']) == 0:
        errors['title'] = "title is required."
    elif len(request.POST['title']) < 2:
        errors['title'] = "title must be at least 2 characters in length."
        print(errors)
    else:
        title = request.POST['title']
        description = request.POST['description']
        some_data = Books.objects.create(title = title, description= description)

    return redirect("/index")

def view_detail(request, pk):

    some_data = Books.objects.get(id=pk)
    some_data_in_Author = Authors.objects.all()
    Added_author= some_data.publishers.all()

    context ={
        "contex":some_data,
        "contex_author":some_data_in_Author,
        "added_author":Added_author
    }
    return render(request, "View_book.html", context)

# Author funtions

def index_Author(request ):

    some_data_in_Author = Authors.objects.all()

    context ={
        "contex_author":some_data_in_Author
    }
    return render(request, "index_Author.html", context)

def create_authors(request):
    errors = {}
    if len(request.POST['first_name']) == 0:
        errors['title'] = "First name is required."
    elif len(request.POST['last_name']) == 0:
        errors['title'] = "last name is required."
    elif len(request.POST['notes']) == 0:
        errors['title'] = "note is required."
    elif len(request.POST['first_name']) < 2:
        errors['title'] = "First name must be at least 2 characters in length."
    elif len(request.POST['last_name']) < 2:
        errors['title'] = "last name must be at least 2 characters in length."
    
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        some_data = Authors.objects.create(first_name = first_name, last_name = last_name, notes = notes )

    return redirect("/index_one")

def view_detail_author(request, pk):
    some_data_in_Author = Authors.objects.get(id=pk)
    some_data = Books.objects.all()
    Added_books= some_data_in_Author.books.all()

    context ={
        "contex_author":some_data_in_Author,
         "contex":some_data,
         "book_added":Added_books,
    }

    return render(request, "view_Author.html", context)

# ADD BOOK TO THE AUTHOR
def add_Book(request, pk):
    book = request.POST['book']
    add_some_book = Books.objects.get(id=book)
    some_author = Authors.objects.get(id=pk)
    saved_book= some_author.books.add(add_some_book)

    return redirect(f"/show_author/{pk}")

def add_Author(request, pk):
    
    author = request.POST['author']
    add_some_author = Authors.object.get(id= author)
    some_book = Books.objects.get(id=pk)
    seved_author = some_book.publishers.add(add_some_author)

    return redirect(f"/show/{pk}")



