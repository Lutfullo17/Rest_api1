from django.urls import path
from .views import get_info, create_product, list_product, detail_product, update_product, putch_product, delete_product

urlpatterns = [
    path('get-info/', get_info),
    path('create/', create_product),
    path('list/', list_product),
    path('detail/<int:pk>', detail_product),
    path('update/<int:pk>', update_product),
    path('detail/<int:pk>', putch_product),
    path('delete/<int:pk>', delete_product)
]