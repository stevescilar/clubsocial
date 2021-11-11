from django.db import models
from django.db.models import manager
from django.contrib.auth.models import User

#let the games begin haha 
#gameofrows&columns

class Venue(models.Model):
    name = models.CharField('Venue Name',max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code',max_length=15)
    phone_number = models.CharField('Contact',max_length=12,blank=True)
    website = models.URLField('Website link',blank=True)
    email_address = models.EmailField('Email Address',blank=True)

    def __str__(self):
        return self.name

#users
class myClubUser(models.Model):
    first_name = models.CharField('First Name',max_length=120)
    last_name = models.CharField('Last Name',max_length=120)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
     

class Event(models.Model):
    name = models.CharField('Event Name',max_length=120,blank=False)
    event_date = models.DateTimeField('Event Date')
    #create a relationship
    venue = models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    #venue = models.CharField(max_length=120)
    manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    description = models.TextField(blank=True)

    #create a relation btwn users and events ( many user can go to many events)
    attendees = models.ManyToManyField(myClubUser,blank=True)

    def __str__(self):
        return self.name

