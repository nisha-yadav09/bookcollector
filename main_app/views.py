from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import os
import uuid
from .models import Book, Lib, Reader
from .forms import ReaderForm

# Define the home view


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def books_index(request):
  books = Book.objects.all()
  return render(request, 'books/index.html', { 'books': books })

def books_detail(request, book_id):
  book = Book.objects.get(id=book_id)
  id_list = book.libs.all().values_list('id')
  print(id_list)
  # Now we can query for libs whose ids are not in the list using exclude
  libs_book_doesnt_have = Lib.objects.exclude(id__in=id_list)
  print(libs_book_doesnt_have)

  reader_form = ReaderForm()
  return render(request, 'books/detail.html', {
    'book': book,
    'reader_form': reader_form,
    'liber': libs_book_doesnt_have
  })


class BookCreate(CreateView):
  model = Book
  fields = ['title', 'author', 'description', 'genre', 'read']
  success_url = '/books/'

  def form_valid(self, form):
    # let CreateView's form_valid method do its thing
    return super().form_valid(form)

class BookUpdate(UpdateView):
  model = Book
  fields = ['author', 'description', 'genre', 'read']

class BookDelete(DeleteView):
  model = Book
  success_url = '/books/'

def add_reader(request, book_id):
  # create a ModelForm instance using the data in request.POST
  form = ReaderForm(request.POST)
  # validate the form
  if form.is_valid():
    new_reader = form.save(commit=False)
    new_reader.book_id = book_id
    new_reader.save()
  return redirect('detail', book_id=book_id)

def assoc_lib(request, book_id, lib_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Book.objects.get(id=book_id).libs.add(lib_id)
  return redirect('detail', book_id=book_id)