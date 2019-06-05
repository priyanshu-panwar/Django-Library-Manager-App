from datetime import date
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the genre')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    #Foreign Key for Author
    #One book can have only one author but one author can have many books
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary =  models.TextField(max_length=1000, help_text='Write a brief description of book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    #Many to many Field for Genre
    #One Genre can have many books and one book can heavy many genres
    genre = models.ManyToManyField(Genre, help_text='Select a genre')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #Returns the url to access a detail record of this book
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        #Create a string for the genre to display on admin
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'

import uuid #Required for unique book instances

class BookInstance(models.Model):
    #for specific copy of a book
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book')
    #foreign key for book
    #one book can have many copies and one copy will have only one book
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200) #for specific release of the book
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availability',
    )

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today()>self.due_back:
            return True
        return False

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return f'{self.id} ({self.book.title})'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name']

    def get_absolute_url(self):
        #Returns a url to access particular author's instance
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Language(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the language of the book')

    def  __str__(self):
        return self.name
