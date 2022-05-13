from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.

LEVEL = (
  ('S', 'Super Reader'),
  ('A', 'Avid Reader'),
  ('N', 'Novice'),
)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    genre = models.CharField(max_length=100)
    read = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
      return reverse('detail', kwargs={'book_id': self.id})

class Reader(models.Model):
  name = models.CharField(max_length=100)
  date = models.DateField('Date')
  level = models.CharField(
        max_length=1,
        choices=LEVEL,
        default=LEVEL[2][0]
  )
  # create a book_id FK column in the table
  book = models.ForeignKey(
    Book,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"Read by {self.name} on {self.date}"