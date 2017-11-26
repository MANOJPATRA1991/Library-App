from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre


# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate count of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()    # The 'all()' is implied by default.
    genres = Genre.objects.count()

    # Number of visits to this view as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request,
                  'index.html',
                  context={
                      'num_books': num_books,
                      'num_instances': num_instances,
                      'num_instances_available': num_instances_available,
                      'num_authors': num_authors,
                      'genres': genres,
                      'num_visits': num_visits
                  })


class BookListView(generic.ListView):
    """
    View function to list all books
    """
    model = Book
    # Our own name for the list as a template variable
    context_object_name = 'book_list'
    template_name = 'catalog/book_list.html'
    paginate_by = 10


class BookDetailView(generic.DetailView):
    """
    View function to display a book's details
    """
    model = Book
    context_object_name = 'book'
    template_name = 'catalog/book_detail.html'


class AuthorListView(generic.ListView):
    """
    View function to display an author's details
    """
    model = Author
    context_object_name = 'author_list'
    template_name = 'catalog/author_list.html'
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """
    View function to display an author's details
    """
    model = Author
    context_object_name = 'author'
    template_name = 'catalog/author-detail.html'

