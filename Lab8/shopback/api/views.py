from django.http import JsonResponse
from api.models import Product,Category

def product_list(request):
    products=Product.objects.all()
    products_json= [product.to_json() for product in products]
    return JsonResponse(products_json,safe=False)

# def product_detail(request,product_id):
#     for product in products:
#         if product['id']==product_id:
#             return JsonResponse(product,status=200)
#     return JsonResponse({'message': 'Product not found with selected ID'}, status=400) 

def categories_list(request):
    categories=Category.objects.all()
    categories_json=[category.to_js() for category in categories]
    return JsonResponse(categories_json,safe=False)

def product_detail(request,product_id):
    try:
        product=Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message':str(e)},status=400)
    return JsonResponse(product.to_json())


def category_detail(request,category_id):
    try:
        category=Category.objects.get(id=category_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message':str(e)},status=400)
    return JsonResponse(category.to_js())

# def category_products(request,category_id):
#     try:
#         category=Product.objects.get(id=category_id)
#     except Product.DoesNotExist as e:
#         return JsonResponse({'message':str(e)},status=400)
#     return JsonResponse(category.to_json())




def category_products(request,category_id):
    try:
        products=Product.objects.all().filter(category_id_id_id=category_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message':str(e)},status=400)
    products_json= [product.to_json() for product in products]
    return JsonResponse(products_json,safe=False)
