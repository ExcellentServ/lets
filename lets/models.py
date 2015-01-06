
from django.db import models
from lino import dd, rt



class Member(dd.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)
    company = models.CharField(max_length=50,default=None)
    date_joined = models.DateField()

    def __unicode__(self):
        return "%s $s %s" % (self.firstname,self.lastname,self.email)


class Members(dd.Table):
    model = Member


class Place(dd.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.PositiveSmallIntegerField(max_length=6)
    street = models.CharField(max_length=200)
    member = models.ForeignKey(Member)

    def __unicode__(self):
        return "%s, %s, %d, %s." % (self.country,self.city,self.postcode,self.street)


class Places(dd.Table):
    model = Place


class Provider(dd.Model):
    member = models.OneToOneField(Member)

    def __unicode__(self):
        return "Provider: " + self.Member.lastname


class Providers(dd.Table):
    model = Provider

    detail_layout = """
    id lastname place email
    OffersByProvider
    """


class Customer(dd.Model):
    member = models.OneToOneField(Member)

    def __unicode__(self):
        return "Customer:" + self.lastname


class Customers(dd.Table):
    model = Customer

    detail_layout = """
    id lastname place email
    DemandsByCustomer
    """


class Product(dd.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(max_length=11)
    # valid_until = models.DateField(blank=True, null=True)
    customer = models.ManyToManyField(Member,through='Demand',related_name='demanded_products')
    provider = models.ManyToManyField(Member,through='Offer',related_name='offered_products')

    def __unicode__(self):
        return self.name + ": " + self.price


class Products(dd.Table):
    model = Product

    detail_layout = """
    id name price
    OffersByProduct DemandsByProduct
    """


class Offer(dd.Model):
    provider = models.ForeignKey(Member)
    product = models.ForeignKey(Product)
    valid_until = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "%s offered by %s" % (self.product, self.provider)


class Offers(dd.Table):
    model = Offer

class OffersByProvider(Offers):
    master_key = 'provider'


class OffersByProduct(Offers):
    master_key = 'product'


class Demand(dd.Model):
    customer = models.ForeignKey(Member)
    product = models.ForeignKey(Product)
    is_arrive = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s (%s)" % (self.product, self.provider)


class Demands(dd.Table):
    model = Demand


class DemandsByCustomer(Demands):
    master_key = 'customer'


class DemandsByProduct(Demands):
    master_key = 'product'
