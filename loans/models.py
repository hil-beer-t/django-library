from django.db import models

# Create your models here.

# Model: Book
# Attributes: cod*, isbn**, author, title, description, publisher, quantity***, type****, is_only_reference*****, is_borrowed****** created_at, updated_at

# ADRs
# cod* - Even not mentioned at RD makes sense besides ID create a unique cod
# isbn** - Even not mentioned at RD every book has a ISBN
# quantity*** - I think it's more maintainable Quantity be only the result from a COUNT query
# type**** - Even not mentioned at RD makes sense create a type field (magazine, journal, article, book etc) 
# is_only_reference***** - NM at RD, it means "cannot be borrowed" 
# is_borrowed****** - NM at RD, it means "has been borrowed" 

class Book(models.Model):
    cod = models.CharField(max_length=150, blank=False, unique=True)
    isbn = models.CharField(max_length=150, blank=True)
    author = models.CharField(max_length=150, blank=False)
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=True)
    publisher = models.CharField(max_length=150, blank=False)
    type = models.CharField(max_length=100, blank=True)
    is_only_reference = models.BooleanField(default=True)
    is_borrowed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)