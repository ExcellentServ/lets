__author__ = 'drx'
#moved import dd,
from lino import dd


class Members(dd.Table):
    model = 'lets.Member'


class Places(dd.Table):
    model = 'lets.Place'

    detail_layout = """
    id country city postcode street
    PlacesByMember
    """


class Providers(dd.Table):
    model = 'lets.Provider'
    # lastname = Provider
    detail_layout = """
    id lastname email
    PlacesByMember OffersByProvider DemandsByProduct
    """


class Customers(dd.Table):
    model = 'lets.Customer'

    detail_layout = """
    id lastname email
    PlacesByMember DemandsByCustomer
    """


class Products(dd.Table):
    model = 'lets.Product'

    detail_layout = """
    id name price
    OffersByProduct DemandsByProduct DemandsByCustomer
    """


class Offers(dd.Table):
    model = 'lets.Offer'


class Demands(dd.Table):
    model = 'lets.Demand'


class OffersByProvider(Offers):
    master_key = 'provider'


class OffersByProduct(Offers):
    master_key = 'product'


class DemandsByCustomer(Demands):
    master_key = 'customer'


class DemandsByProduct(Demands):
    master_key = 'product'


class PlacesByMember(Places):
    master_key = 'member'

#
# class ProductByProvider(Products):
#     master_key = 'providers'
#
#
# class ProductByCustomer(Products):
#     master_key = 'customers'
