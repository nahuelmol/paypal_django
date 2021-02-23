from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Product, Order

def SimpleCheckout(req):
   	
    return render(req,'base/simple_checkout.html')

def checkout(req):
	product = Product.objects.get(id=pk)
	context = {'product':product}
	return render(req,'base/checkout.html')

def store(req):
	products = Product.object.all()
	context = {'products':products}
	return render(req,'base/store.html',context)

def paymentComplete(req):
	body = json.loads(req.body)
	print('BODY:', body)
	product = Product.objects.get(id=body['productId'])

	Order.objects.create(
		product=product
		)
	return JsonResponse('Payment completed!', safe=False)


