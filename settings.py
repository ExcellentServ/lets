from lino.projects.std.settings import *

ALLOWED_HOSTS = ['*']
class Site(Site):

    title = "Lino LETS Demo"

    def setup_menu(self, ui, profile, main):
        m = main.add_menu("members", "Our Members")
        m.add_action(self.modules.xserv_lets.Providers)
        m.add_action(self.modules.xserv_lets.Customers)

        m = main.add_menu("market", "Market")
        m.add_action(self.modules.xserv_lets.Products)
        m.add_action(self.modules.xserv_lets.Offers)
        m.add_action(self.modules.xserv_lets.Demands)


        m = main.add_menu("location", "Browse by Location")
        m.add_action(self.modules.xserv_lets.Places)

    # def get_admin_main_items(self):
    #
    #     yield self.modules.lets.ActiveProducts

SITE = Site(globals(), 'xserv_lets')

DEBUG = True

