from django.forms import ModelForm
from .models import Reader, Book

class ReaderForm(ModelForm):
  class Meta:
    model = Reader
    fields = ['name', 'date', 'level']