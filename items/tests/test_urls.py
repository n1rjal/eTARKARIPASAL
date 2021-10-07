from django.test import SimpleTestCase
from django.urls import reverse,resolve
from items.views import home, addtocart,removefromcart,cart,getcurrtransaction,bill,sucess,export,search,about

class Test_Items_Urls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('homepage') 
        self.assertEquals(resolve(url).func,home)
    def test_cart_url_resolves(self):
        url = reverse('cart') 
        self.assertEquals(resolve(url).func,cart)
    def test_cart_transaction_url_resolves(self):
        url = reverse('currentcart') 
        self.assertEquals(resolve(url).func,getcurrtransaction)
    def test_bill_url_resolves(self):
        url = reverse('bill') 
        self.assertEquals(resolve(url).func,bill)
    def test_sucess_url_resolves(self):
        url = reverse('sucess') 
        self.assertEquals(resolve(url).func,sucess)
    def test_export_url_resolves(self):
        url = reverse('export') 
        self.assertEquals(resolve(url).func,export)
    def test_search_url_resolves(self):
        url = reverse('search') 
        self.assertEquals(resolve(url).func,search)
    def test_about_url_resolves(self):
        url = reverse('about') 
        self.assertEquals(resolve(url).func,about)
    