
from django.db import models
#why we import it?!
# from lino import rt
from lino.utils.mti import EnableChild
from .tables import *


class Member(dd.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)
    date_joined = models.DateField()
    #to support one to one
    is_provider = EnableChild('Provider', verbose_name="is a provider")
    is_customer = EnableChild('Customer', verbose_name="is a customer")

    def __unicode__(self):
        return "%s %s %s" % (self.firstname, self.lastname, self.email)


class Place(dd.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.PositiveSmallIntegerField(max_length=6)
    street = models.CharField(max_length=200)
    member = models.ForeignKey(Member)

    def __unicode__(self):
        return "%s, %s, %d, %s." % (self.country,self.city,self.postcode,self.street)


# class Provider(dd.Model):
class Provider(Member):
    company = models.CharField(max_length=50,default=None)

    def __unicode__(self):
        return "Provider: %s" % self.lastname


# class Customer(dd.Model):
class Customer(Member):
    anything = models.CharField(max_length=50,blank=True)

    def __unicode__(self):
        return "Customer: %s" % self.lastname

class Product(dd.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(max_length=11)
    # valid_until = models.DateField(blank=True, null=True)
    customers = models.ManyToManyField(Customer,through='Demand',related_name='demanded_products')
    providers = models.ManyToManyField(Provider,through='Offer',related_name='offered_products')

    def __unicode__(self):
        return "{} : {}".format(self.name,self.price)


class Offer(dd.Model):
    provider = models.ForeignKey(Provider)
    product = models.ForeignKey(Product)
    valid_until = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "%s offered by %s" % (self.product, self.provider)



class Demand(dd.Model):
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    is_arrive = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s (%s)" % (self.product, self.provider)