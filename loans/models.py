from django.db import models

# Create your models here.

# Model: Book
# TODO - add category and reserved attribute
# Attributes: cod*, isbn**, author, title, description, publisher, quantity***, type****, is_only_reference*****, is_borrowed****** created_at, updated_at

# ADRs
# author should be another table with a MANY-TO-MANY relation with book
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

    def __str__(self) -> str:
        return self.title + " - " + self.cod

class AppUser(models.Model):
    mat = models.CharField(max_length=100, blank=False, unique=True)
    name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email

class Loan(models.Model):
    start_time = models.DateField(auto_now=False, auto_now_add=False, null=False)
    end_time = models.DateField(auto_now=False, auto_now_add=False, null=False)
    is_returned = models.BooleanField()
    ok_returned = models.BooleanField()
    days_late = models.PositiveSmallIntegerField()
    app_user = models.ForeignKey(AppUser, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.app_user.email + " - " + self.book.title + " - " + self.book.cod[-4:]
