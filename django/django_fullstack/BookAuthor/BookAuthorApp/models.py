from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=255)
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"<Book object: {self.title} ({self.id})"

class Author(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  notes = models.TextField(default="BestSeller")
  books = models.ManyToManyField(Book, related_name = "writer")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"<Author object: {self.first_name} ({self.id})"