from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='homepage'),
    path('addtocart/<id>',views.addtocart,name="addtocart"),
    path('removefromcart/<id>',views.removefromcart,name="removefromcart"),
    path('cart/',views.cart,name="cart"),
    path('currentcart/',views.getcurrtransaction,name="currentcart"),
    path('bill/',views.bill,name='bill'),
    path('sucess/',views.sucess,name="sucess"),
    path('export/',views.export,name="export"),
    path('search/',views.search,name='search'),
    path('about/',views.about,name='about')
]
