from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.auth.models import User
from . models import Book, Loan

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['cod', 'isbn', 'author', 'title', 'publisher', 'type']

class LoanForm(forms.ModelForm):

    required_css_class = 'required'

    user_pk = models.ForeignKey(User, on_delete=models.RESTRICT, default=2)
    book_pk = models.ForeignKey(Book, on_delete=models.RESTRICT)

    start_time = forms.DateField(
        label='Start date',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            }),
            input_formats=('%Y-%m-%d',),
    )
    end_time = forms.DateField(
        label='End date',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            }),
            input_formats=('%Y-%m-%d',),
    )

    class Meta:
        model = Loan
        fields = ['start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'