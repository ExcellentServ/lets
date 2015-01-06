# -*- coding: UTF-8 -*-
from lino.dd import resolve_model


def findbyname(model, name):
    """
    Utility function.
    """
    return model.objects.get(name=name)

def findbyid(model, id):
    """
    Utility function.
    """
    return model.objects.get(id=id)


def objects():
    """
    This will be called by the :ref:`dpy` deserializer and 
    must yield a list of object instances to be saved.
    """
    Place = resolve_model('lets.Place')
    Member = resolve_model('lets.Member')
    Provider = resolve_model('lets.Provider')
    Customer = resolve_model('lets.Customer')
    Product = resolve_model('lets.Product')
    Offer = resolve_model('lets.Offer')
    Demand = resolve_model('lets.Demand')

    yield Place(country="Egypt",city="New Cairo",postcode="11212",street="3rd settlment")
    yield Place(country="Estonia",city="New City",postcode="11212",street="High Way")
    # yield Place(name="Tartu")
    # yield Place(name="Vigala")
    # yield Place(name="Haapsalu")
    yield Member(id=1,firstname="Mahmoud",lastname="Mamdouh",email="sharedup@gmail.com",company="Excllent Serv")
    yield Member(id=2,firstname="Luc",lastname="Saffre",email="luc@gmail.com",company="Lino")


    yield Provider(member=findbyid(Member, 1))
    # yield Provider(name="Argo", place=findbyname(Place, "Haapsalu"))
    # yield Provider(name=u"Tõnis", place=findbyname(Place, "Vigala"))
    # yield Provider(name="Anne", place=findbyname(Place, "Tallinn"))
    # yield Provider(name="Jaanika", place=findbyname(Place, "Tallinn"))

    yield Customer(member=findbyid(Member, 2))
    # yield Customer(name="Henri", place=findbyname(Place, "Tallinn"))
    # yield Customer(name="Mare", place=findbyname(Place, "Tartu"))
    # yield Customer(name=u"Külliki", place=findbyname(Place, "Vigala"))

    yield Product(name="USB",price="100")
    yield Product(name="HDD",price="350")
    yield Product(name="RAM",price="200")

    yield Offer(product=findbyname(Product, "USB"), provider=findbyid(Provider, 1))
    yield Offer(product=findbyname(Product, "RAM"), provider=findbyid(Provider, 1))
    # yield Offer(product=findbyname(Product, "Tatar"), provider=findbyname(Provider, "Priit"))
    # yield Offer(product=findbyname(Product, "Tatar"), provider=findbyname(Provider, "Anne"))

    yield Demand(product=findbyname(Product, "RAM"), customer=findbyid(Customer, 2))
    # yield Demand(product=findbyname(Product, "Kanamunad"), customer=findbyname(Customer, "Henri"))
    # yield Demand(product=findbyname(Product, "Kanamunad"), customer=findbyname(Customer, "Mare"))
