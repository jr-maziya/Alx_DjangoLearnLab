from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic import DetailView

# Create your views here.
def book_list_view(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)

class LibraryDetails_view(DetailView):
  """A class-based view for displaying details of a specific library."""
  model = Library
  template_name = 'relationship_app/library_detail.html'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the library."""
    context = super().get_context_data(**kwargs)  # Get default context data
    book = self.get_object()  # Retrieve the current book instance
    context['average_rating'] = book.get_average_rating() 

