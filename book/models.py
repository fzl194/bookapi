from django.db import models

# Create your models here.
class Book(models.Model):
    isbn  = models.CharField(max_length=13, unique = True, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    logo = models.TextField(null=True)
    publisher = models.CharField(max_length=100, null=True)
    published = models.CharField(max_length=20,null=True)
    page = models.CharField(max_length=10, null=True)
    price = models.CharField(max_length=10, null=True)
    designed = models.CharField(max_length=20, null=True)
    description = models.TextField(null = True, default="")
    class Meta: 
        db_table = 'book'



