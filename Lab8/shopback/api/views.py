import imp
from telnetlib import STATUS
from django.http.response  import JsonResponse
from django.http.request import HttpRequest
from api.models import Product

def product_list(request):
    products=Product.objects.all()
    print(products)
    return JsonResponse(products,safe=False)

def product_detail(request,product_id):
    for product in products:
        if product['id']==product_id:
            return JsonResponse(product,status=200)
    return JsonResponse({'message': 'Product not found with selected ID'}, status=400) 