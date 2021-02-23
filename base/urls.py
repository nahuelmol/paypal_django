from django.urls import path
from . import views

urlpatterns = [
	path('simple-checkout/',views.SimpleCheckout),


	path('',views.store, name="store"),
	path('checkout/<int:pk>/',views.checkout),
	path('complete/',views.paymentComplete,name="complete"),
]