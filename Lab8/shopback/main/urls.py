
from django.urls import path,re_path
from main.views import show_time
from main.views import Hello,product_list,product_detail

urlpatterns = [
    path('hi/',Hello ),
    re_path('time/plus/(\d{1,2})/',show_time),
    path('products/',product_list),
    path('products/<int:product_id>',product_detail)
]