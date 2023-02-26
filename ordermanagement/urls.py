"""ordermanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from orderticket import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginPage, name="login"),
    path('', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    #path('ajaxform/',views.formCalculation,name='formCalculation'),
    #path('dashboard',views.dashboard,name="dashboard"),
    #path('newCustomerAdmin/', views.newCustomerAdmin, name="newCustomerAdmin"),
    #path('customer/<str:pk_test>/', views.customer, name="customer"),
    #path('customerorders/<str:pk_test>/', views.customerOrder, name="customerOrder"),
    #path('changepassword/<str:username>/', views.change_password, name="changepassword"),
    #path('customer/delete/<int:id>/',views.deleteCustomer, name='deleteCustomer'),
    #path('order/delete/<int:id>/',views.deleteOrder, name='deleteOrder'),
    #path('pastorders/',views.pastorders,name='pastorders'),
    #path('customerpastorders/',views.customerpastorders,name='customerpastorders'),
    path('OptionChainSingle/', views.optionChain, name='optionChain'),
    path('equity/', views.equity, name='equity'),
    path('secondhome/', views.secondhome, name='secondhome'),
    path('seconoptionChain/', views.seconoptionChain, name='seconoptionChain'),
    path('secondequity/', views.secondequity, name='secondequity'),
    
    
]
