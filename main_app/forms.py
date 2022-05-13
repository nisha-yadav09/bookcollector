from django.forms import ModelForm
from .models import Reader

class ReaderForm(ModelForm):
  class Meta:
    model = Reader
    fields = ['name', 'date', 'level']