from django.db import models

# Define models here
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

class FullTime(models.Model):
    accepted_offer = models.ForeignKey('Company')#stores company information for the offer accepted (FK to CompanyID)
    offers_received = models.IntegerField()#number of offers received
    date_accepted = models.DateField
