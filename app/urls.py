from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.home, name='home'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('payment/<int:mode>/', views.payment, name='payment'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('buy_now_payment/<int:pk>/<int:mode>/',
         views.buy_now_payment, name='buy_now_payment'),
    path('buynow/<int:pk>', views.buy_now, name='buynow'),
    path('profile/', views.profile, name='profile'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('address/', views.address, name='address'),
    path('delete_adress/<int:pk>/', views.delete_adress, name='delete_adress'),
    path('orders/', views.orders, name='orders'),
    path('order_cancelation/<int:pk>/',
         views.order_cancelation, name='order_cancelation'),
    path('return_product/<int:pk>/', views.return_product, name='return_product'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('plus_cart/', views.plus_cart, name='plus_cart'),
    path('minus_cart/', views.minus_cart, name='minus_cart'),
    path('remove_cart/', views.remove_cart, name='remove_cart'),
    path('wired/', views.wired, name='wired'),
    path('wired/<slug:data>/', views.wired, name='wired_data'),
    path('bluetooth/', views.bluetooth, name='bluetooth'),
    path('bluetooth/<slug:data>/', views.bluetooth, name='bluetooth_data'),
    path('earpodes/', views.earpodes, name='earpodes'),
    path('earpodes/<slug:data>/', views.earpodes, name='earpodes_data'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('checkout/', views.checkout, name='checkout'),
    path('otp/', views.otp, name='otp'),
    path('search/', views.search, name='search'),
    path('check_otp/', views.check_otp, name='check_otp'),
    path('user_logout/', views.user_logout, name='user_logout'),

]
