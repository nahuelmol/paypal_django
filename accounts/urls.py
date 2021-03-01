from django.urls import path
from . import views

urlpatterns = [
	path('register/',views.registerPage,name='register'),
	path('login/',views.loginPage,name='login'),
	path('home/',views.Home,name='home'),
	path('home/profile',views.profile,name='profile'),
	path('home/feed/customer',views.customerPage,name='customer_page'),
	path('home/feed/vendor',views.vendorPage,name='vendor_page'),
	path('logout/',views.logoutPage,name='logout')
]