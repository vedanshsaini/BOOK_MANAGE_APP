from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.decorators.http import require_POST

from books.forms import BookForm
@login_required
def profile_view(request):
    # Fetch all reading lists associated with the current user
    reading_lists = ReadingList.objects.filter(user=request.user)

    context = {
        'reading_lists': reading_lists
    }
    return render(request, 'registration/profile.html', context)

from .models import Book, ReadingList

class BookListView(generic.ListView):
    model = Book
    template_name = 'registration/book_list.html'
    context_object_name = 'book_list'

class ReadingListListView(generic.ListView):
    model = ReadingList
    template_name = 'reading_lists/reading_list_list.html'
    context_object_name = 'reading_list_list'

    def get_queryset(self):
        return ReadingList.objects.filter(user=self.request.user)

@login_required
def add_book_to_list(request, pk):
    reading_list = get_object_or_404(ReadingList, pk=pk, user=request.user)
    book_id = request.POST.get('book_id')
    if book_id:
        book = get_object_or_404(Book, id=book_id)
        reading_list.books.add(book)
    return redirect('reading_list_list')

@login_required
def remove_book_from_list(request, list_pk, book_pk):
    reading_list = get_object_or_404(ReadingList, pk=list_pk, user=request.user)
    book = get_object_or_404(Book, pk=book_pk)
    reading_list.books.remove(book)
    return redirect('reading_list_list')


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class CustomLoginView(BaseLoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile')

class LogoutView(BaseLogoutView):
    template_name = 'registration/logout.html'
    next_page = reverse_lazy('index')

def index(request):
    return render(request, 'index.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Process the form data and save the new book
            form.save()
            return redirect('book_list')  # Redirect to the book list page after adding the book
    else:
        form = BookForm()
    return render(request, 'registration/add_book.html', {'form': form})