from django.urls import path

from django.contrib import admin
from . import views
from .views import product_detail, product_list, product_search, success

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('success/', success, name='success'),
    path('track/', views.track, name="track"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('product-list/', views.product_list, name='product_list'),
    path('admin/', admin.site.urls),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/search/', product_search, name='product_search'), 
    path('index/', views.homepage, name='index'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),

]