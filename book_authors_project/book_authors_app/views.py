from django.shortcuts import render, redirect, HttpResponse
from book_authors_app.models import Book, Author

# Create your views here.

def index(request):
    info = Book.objects.all()
    context = {
        'all_books': info,
    }
    return render(request, 'index.html', context)

def add_book(request):
    Book.objects.create(title=request.POST["title"], desc=request.POST["desc"])
    return redirect('/')

def books(request,number):
    request.session['number'] = number
    info = Book.objects.get(id=request.session['number'])
    info_authors = info.authors.all()
    all_authors = Author.objects.all()
    context = {
        'book': info,
        'current_authors': info_authors,
        'all_authors': all_authors,
    }
    return render(request, 'books.html', context)

def add_author_to_book(request):
    # print("book ID:", request.session['number'])
    # print("author ID:", request.POST['author_1'])
    book_id = request.session['number']
    author_id = int(request.POST['author_1'])
    new_author = Author.objects.get(id=author_id)
    info = Book.objects.get(id=book_id)
    info.authors.add(new_author)
    return redirect('/')

def author(request):
    data = Author.objects.all()
    context = {
        'all_authors': data, 
    }
    return render(request, 'authors.html', context)

def add_author(request):
    print(request)
    print(request.POST)
    Author.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], notes=request.POST["notes"])
    return redirect('/author')

def view_author(request, number2):
    request.session['number2'] = number2
    data = Author.objects.get(id=request.session['number2'])
    data_books = data.books.all()
    data_all_books = Book.objects.all()
    context = {
        'author_view': data,
        'current_books': data_books,
        'all_author_books': data_all_books,
    }
    return render(request, 'view_authors.html', context)

def add_book_to_author(request):
    # print("author ID:", request.session['number2'])
    # print("book ID:", request.POST['book_added'])
    author_id_ = request.session['number2']
    book_added_id = int(request.POST['book_added'])
    new_book = Book.objects.get(id=book_added_id)
    data = Author.objects.get(id=author_id_)
    data.books.add(new_book)
    return redirect('/author')
