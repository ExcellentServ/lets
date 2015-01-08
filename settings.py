from lino.projects.std.settings import *


class Site(Site):

    title = "Lino LETS Demo"

    def setup_menu(self, ui, profile, main):
        m = main.add_menu("members", "Our Members")
        m.add_action(self.modules.lets.Providers)
        m.add_action(self.modules.lets.Customers)

        m = main.add_menu("market", "Market")
        m.add_action(self.modules.lets.Products)
        m.add_action(self.modules.lets.Offers)
        m.add_action(self.modules.lets.Demands)


        m = main.add_menu("location", "Browse by Location")
        m.add_action(self.modules.lets.Places)

    # def get_admin_main_items(self):
    #
    #     yield self.modules.lets.ActiveProducts

SITE = Site(globals(), 'lets')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lets',
	'USER': 'root',
    }
}
DEBUG = True

