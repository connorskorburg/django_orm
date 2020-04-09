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

def add_author(request):
    # print("book ID:", request.session['number'])
    # print("author ID:", request.POST['author'])
    book_id = request.session['number']
    author_id = int(request.POST['author'])
    new_author = Author.objects.get(id=author_id)
    info = Book.objects.get(id=book_id)
    info.authors.add(new_author)
    # print(info.authors.all())
    return redirect('/')