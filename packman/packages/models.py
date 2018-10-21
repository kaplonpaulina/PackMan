from django.db import models

# Create your models here.


class Package(models.Model):
    sender_id = models.CharField(max_length=150)
    driver_id = models.CharField(max_length=150)
    opinion = models.CharField(max_length=500)
    date_registration = models.DateField()
    date_start_of_delivery = models.DateField()
    date_end_of_delivery = models.DateField()
    state = models.CharField(max_length=20)
    description = models.CharField(max_length=500)

    def __str__(self):
        return 'Package sent by : %s , delivered by: %s \n  ' % (self.sender_id, self.driver_id)
