from django.db import models
from account.models import Customer
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    
    author_description = models.TextField(null=True)
    
    
    def __str__(self):
        return self.first_name
    
    
class Book(models.Model):
    
    class Categorie(models.TextChoices):
        ADVENTURE = 'Adventure'
        CLASSIC = 'Classic'
        FANTASY = 'Fantasy'
        ROMANCE = 'Romance'
        HORROR = 'Horror'
        COMIC = 'Comic'
        SCIENCE = 'Science'
        LITERATURE ='literature'
        
        
    title = models.CharField(max_length=200, null=True)
    isbn13 = models.CharField(max_length=14, null=True)
    description = models.TextField(null=True)
    is_popular = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)
    categorie = models.CharField(
        max_length=20,
        choices=Categorie.choices,
        default=Categorie.CLASSIC
    )
    
    book_image =  models.ImageField(upload_to ='static/images/')
    book_language = models.CharField(max_length=25, null=True)
    num_pages = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    
    author = models.ManyToManyField(Author)
    
    def __str__(self) -> str:
        return self.title
    
   
    
    
    
  
class CustomerOrder(models.Model):
    order_date = models.DateField()
    destination_address = models.CharField()
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id


class OrderLine(models.Model):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)




    
    