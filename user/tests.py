from django.test import TestCase

# Create your tests here.
## URLS TESTING OF USER APP
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from user.views import adduser,login,authuser,logout,profile,update,searchuser
import user.models

class Test_User_Urls(SimpleTestCase):
    def test_signup_url_resolves(self):
        url = reverse('signup') 
        self.assertEquals(resolve(url).func,adduser)
    def test_login_url_resolves(self):
        url = reverse('_login') 
        self.assertEquals(resolve(url).func,login)
    def test_authuser_url_resolves(self):
        url = reverse('login') 
        self.assertEquals(resolve(url).func,authuser)
    def test_logout_url_resolves(self):
        url = reverse('logout') 
        self.assertEquals(resolve(url).func,logout)
    def test_profile_url_resolves(self):
        url = reverse('profile') 
        self.assertEquals(resolve(url).func,profile)
    def test_update_url_resolves(self):
        url = reverse('update_profile') 
        self.assertEquals(resolve(url).func,update)
    # def test_searchuser_url_resolves(self):
    #     # url = reverse('searchuser',args=[?P<user_name>\) 
        
    #     # self.assertEquals(resolve(url).func,searchuser)
    #     print(resolve('searchuser'))
    
     