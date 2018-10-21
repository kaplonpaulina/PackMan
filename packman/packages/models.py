from django.db import models

# Create your models here.


class Package(models.Model):
    sender_id = models.CharField(max_length=150)
    driver_id = models.CharField(max_length=150)
    opinion = models.CharField(max_length=500, blank=True)
    date_registration = models.DateField(blank=True)
    date_start_of_delivery = models.DateField(blank=True)
    date_end_of_delivery = models.DateField(blank=True)
    state = models.CharField(max_length=20,blank=True)
    description = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return 'Paczka nada przez : %s , zawiezioina przez: %s \n  ' % (self.sender_id, self.driver_id)
