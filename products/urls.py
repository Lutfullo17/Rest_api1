from django.urls import path
# from .views import get_info, create_product, list_product, detail_product, update_product, putch_product, delete_product
from .views import ProductListView, ProductCreateView, ProductDetailView, ProductDelateView, ProductUpdateView

urlpatterns = [
    path('list/', ProductListView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('detail/<int:pk>', ProductDetailView.as_view()),
    path('delete/<int:pk>', ProductDelateView.as_view()),
    path('update/<int:pk>', ProductUpdateView.as_view()),
]

# from rest_framework import routers
# from .views import ProductViewSet
#
# router = routers.SimpleRouter()
# router.register(r'product-w', ProductViewSet)
# urlpatterns = router.urls