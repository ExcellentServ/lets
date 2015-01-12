# -*- coding: UTF-8 -*-
from lino.dd import resolve_model
#add datetime
from datetime import datetime
from lino.utils import mti

def findbyname(model, name):
    """
    Utility function.
    """
    return model.objects.get(name=name)

def findbyemail(model, email):
    """
    Utility function.
    """
    return model.objects.get(email=email)


def objects():
    """
    This will be called by the :ref:`dpy` deserializer and 
    must yield a list of object instances to be saved.
    """
    Place = resolve_model('lets.Place')
    Member = resolve_model('lets.Member')
    Pro = resolve_model('lets.Provider')
    Cus = resolve_model('lets.Customer')
    Product = resolve_model('lets.Product')
    Off = resolve_model('lets.Offer')
    Dem = resolve_model('lets.Demand')

    yield Pro(firstname="Mahmoud", lastname="Mamdouh", email="sharedup@gmail.com",company="Excellent Serv", date_joined= datetime.now())
    yield Cus(firstname="Luc", lastname="Saffre", email="luc@gmail.com", date_joined=datetime.now())


    yield Place(country="Egypt",city="New Cairo",postcode="11212",street="3rd settlment",member=findbyemail(Member, "sharedup@gmail.com"))
    yield Place(country="Egypt",city="New Cairo",postcode="11215",street="3rd settlment",member=findbyemail(Member, "sharedup@gmail.com"))
    yield Place(country="Estonia",city="New City",postcode="11212",street="High Way",member=findbyemail(Member, "luc@gmail.com"))
    # yield Place(name="Tartu")
    # yield Place(name="Vigala")
    # yield Place(name="Haapsalu")

    def provider(who,company):
        return Pro(
            member = findbyemail(Member,who),
            company=company
        )

    # mti.insert_child(Pro(1,"Excllent Serv"),Pro)
    # yield Provider(name="Argo", place=findbyname(Place, "Haapsalu"))
    # yield Provider(name=u"Tõnis", place=findbyname(Place, "Vigala"))
    # yield Provider(name="Anne", place=findbyname(Place, "Tallinn"))
    # yield Provider(name="Jaanika", place=findbyname(Place, "Tallinn"))

    def customer(who):
        return Cus(
            member = findbyemail(Member,who)
        )
    # yield mti.insert_child(Cus(2), Cus)
    # yield Customer(name="Henri", place=findbyname(Place, "Tallinn"))
    # yield Customer(name="Mare", place=findbyname(Place, "Tartu"))
    # yield Customer(name=u"Külliki", place=findbyname(Place, "Vigala"))

    yield Product(name="USB",price="100")
    yield Product(name="HDD",price="350")
    yield Product(name="RAM",price="200")

    def offer(what, who):
        return Off(
            provider = findbyemail(Pro, who),
            product = findbyname(Product, what)
        )

    yield offer("USB", "sharedup@gmail.com")
    # yield Offer(product=findbyname(Product, "RAM"), provider=findbyid(Provider, 1))
    # yield Offer(product=findbyname(Product, "Tatar"), provider=findbyname(Provider, "Priit"))
    # yield Offer(product=findbyname(Product, "Tatar"), provider=findbyname(Provider, "Anne"))
    def demand(what, who):
        return Dem(
            customer = findbyemail(Cus, who),
            product = findbyname(Product, what)
        )

    yield demand("RAM", "luc@gmail.com")
    # yield Demand(product=findbyname(Product, "Kanamunad"), customer=findbyname(Customer, "Henri"))
    # yield Demand(product=findbyname(Product, "Kanamunad"), customer=findbyname(Customer, "Mare"))
