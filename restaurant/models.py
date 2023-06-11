from django.db import models

# Create your models here.
class Booking(models.Model):
    id          = models.IntegerField(primary_key=True)
    name        = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    bookingDate = models.DateTimeField()
    
class Menu(models.Model):
    id           = models.IntegerField(primary_key=True)
    title        = models.CharField(max_length=255)
    price        = models.DecimalField(max_digits = 5,
                         decimal_places = 2)
    inventory    = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'