from django.db import models

#class Prices

#class Homedescriptions
class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name

class Prices(models.Model):
    description = models.CharField(max_length=400, blank=True)
    services = models.CharField(max_length=400, blank=True)
    prices = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos', null=True)

    def __str__(self):
        return self.services

class Descriptions(models.Model):
    e_mail = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    home_page_description = models.CharField(max_length=400, blank=True)




