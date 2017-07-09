from django.db import models

class Location(models.Model):
    pincode=models.CharField(max_length=20)
    country=models.CharField(max_length=100)


    def __str__(self):
        return self.pincode+"-"+self.country




