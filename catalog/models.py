from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Hdd(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    name = models.CharField(max_length=200)
    borrower = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('hdd-detail', args=[str(self.id)])
    
    def get_update_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('hdd_update', args=[str(self.id)])    
    
    class Meta:
        ordering = ['name']    
        
        
class Facility(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('facility-detail', args=[str(self.id)])
    
    def get_update_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('facility_update', args=[str(self.id)])    
    
    class Meta:
        ordering = ['name']            