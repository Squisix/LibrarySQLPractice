from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    isbn = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication_year = models.DateTimeField()
    publisher = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    small_image_url = models.CharField(max_length=100)
    medium_image_url = models.CharField(max_length=100)
    large_image_url = models.CharField(max_length=100)
   
    def __str__(self):
        text = '{0} ({1})'
        return text.format(self.title, self.isbn)
    
class Member(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    birth_date = models.DateTimeField()
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    member_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    memebership_type = models.CharField(max_length=50)
    borrowed_books = models.SmallIntegerField()
    
    def __str__(self):
        text = '{0} {1} ({2})'
        return text.format(self.first_name, self.last_name, self.id)
    
class Borrow(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField()
    issue = models.CharField(max_length=150)
    
    
    def __str__(self):
        text = '{0} {1} ({2})'
        return text.format(self.book_id, self.member_id, self.borrow_date)