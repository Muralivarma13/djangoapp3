from django.db import models
import uuid

# Create your models here.

class OrderDetails(models.Model):
    usermail=models.EmailField(unique=True)
    orderid=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    mode=models.CharField(max_length=50)
    status=models.CharField(max_length=80)
    dateandtime=models.DateTimeField(auto_now_add=True)
    currency=models.CharField(default="INR",max_length=50)
    transaction_id=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)




class MovieBooking(models.Model):
    moviename=models.CharField(max_length=100)
    showtime=models.CharField(max_length=100)  
    screenname=models.CharField(max_length=100)
    dateandtime=models.DateTimeField(auto_now_add=True)
    transaction_id=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)


class BookDetails(models.Model):
    bookname=models.CharField(max_length=50)
    price=models.CharField(default="INR",max_length=50)  
    author=models.CharField(max_length=100)
    type=models.CharField(max_length=50) 