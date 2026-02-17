from django.core.serializers import serialize
from django.shortcuts import render ,get_object_or_404
from django.template.defaultfilters import title
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK

from .serializers import Product, ProductSerializer
from rest_framework.exceptions import ValidationError
from .models import Product
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, \
    UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from decimal import Decimal
from django.db.models import Q



# uy ishi

class ProductLictCreateView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        products =  self.get_queryset()
        serializer = self.get_serializer(products, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class ProductDetailView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get_object(self, request, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Topilmadi'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = self.get_serializer(product)
        return Response(serializer.data)

    def put(self,request, pk):
        product = self.get_object(pk)
        serializer = self.get_serializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        product = self.get_object(pk=pk)
        product.delete()
        return Response({'massage': 'Ochirildi'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        products = self.get_queryset()
        search = request.query_params.get('search')
        if search:
            products = products.filter(title__icontains=search)

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
























# class ProductListCreateView(GenericAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#
#     def get(self, request):
#         search = self.request.query_params.get('search', None)
#         price = self.request.query_params.get('price')
#         if price:
#             price = Decimal(price)
#
#         if search:
#             product = Product.objects.filter(
#                 Q(title__icontains=search) & Q(price__gte=price)
#             )
#             if not product.exists():
#                 data = {
#                     'status': status.HTTP_400_BAD_REQUEST,
#                     'message': 'Topilmadi',
#                 }
#
#                 return Response(data, status=status.HTTP_400_BAD_REQUEST)
#             serializer = self.get_serializer(product, many=True)
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'message': 'Products',
#                 "data": serializer.data
#             }
#
#             return Response(data)
#         product = self.get_queryset()
#         serializer = self.get_serializer(product, many=True)
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'Products',
#             "data": serializer.data
#         }
#
#         return Response(data)
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_201_CREATED,
#                 'message': 'Product',
#                 "data": serializer.data
#             }
#             return Response(data)
#
#         data = {
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Eror',
#             "desc": serializer.errors
#         }
#
#         return Response(data)


# class ProductListView(APIView):
#     def get(self, request):
#         product = Product.objects.all()
#         serializer = ProductSerializer(product, many=True)
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'products',
#             'data': serializer.data
#         }
#         return Response(data)
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_201_CREATED,
#                 'message': 'Products',
#                 'data': serializer.data
#             }
#             return Response(data)
#         data = {
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'error',
#             'desc': serializer.errors
#         }
#         return Response(data)
#
# class ProductCreateView(APIView):
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_201_CREATED,
#                 'message': 'Products',
#                 'data': serializer.data
#             }
#             return Response(data)
#         data = {
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'error',
#             'desc': serializer.errors
#         }
#         return Response(data)

# class ProductUpdateDetailDestroyView(GenericAPIView):
#     serializer_class = ProductSerializer
#
#     def get_object(self, pk):
#         product = Product.objects.filter(pk=pk).first()
#         return
#
#     def put(self, request, pk):
#         product = self.get_object(pk)
#         serializer = self.get_serializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'product update',
#             'data':serializer.data
#         }
#         return Response(data)
#
#     def patch(self, request, pk):
#         product = self.get_object(pk)
#         serializer = self.get_serializer(product, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'product update',
#             'data':serializer.data
#         }
#         return Response(data)
#
#     def get(self, request, pk):
#         user = self.get_object(pk)
#         serializer = self.get_serializer(user)
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'user',
#             'data': serializer.data
#         }
#         return Response(data)
#
#     def delete(self, request, pk):
#         user = self.get_object(pk)
#         if user is None:
#             data = {
#                 'status': status.HTTP_404_NOT_FOUND,
#                 'message': 'user topilmadi'
#             }
#             return Response(data)
#         user.delete()
#         data = {
#             'status': status.HTTP_204_NO_CONTENT,
#             'message': 'user topilmadi',
#             'data': user
#         }
#         return Response(data)




# class ProductDetailView(APIView):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product)
#         data = {
#             'status': status.HTTP_200_OK,
#             'data': serializer.data
#         }
#         return Response(data)
#
#
#
# class ProductDelateView(APIView):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         product.delete()
#         data = {
#             'status': status.HTTP_204_NO_CONTENT,
#             'message': 'Product delete'
#         }
#         return Response(data)
#


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer



# class ProductListView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductCreateView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDelateView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductUpdateDetailDestroyView(GenericAPIView):
#     serializer_class = ProductSerializer
#
#     def get_object(self, pk):
#         product = Product.objects.filter(pk=pk).first()
#         return product
#
#     def put(self, request, pk):
#         product = self.get_object(pk)
#         serializer = self.get_serializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'product update',
#             'data':serializer.data
#         }
#         return Response(data)
#
#     def patch(self, request, pk):
#         product = self.get_object(pk)
#         serializer = self.get_serializer(product, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'product update',
#             'data':serializer.data
#         }
#         return Response(data)
#
#     def get(self, request, pk):
#         user = self.get_object(pk)
#         serializer = self.get_serializer(user)
#         data = {
#             'status': status.HTTP_200_OK,
#             'message': 'user',
#             'data': serializer.data
#         }
#         return Response(data)
#
#     def delete(self, request, pk):
#         user = self.get_object(pk)
#         if user is None:
#             data = {
#                 'status': status.HTTP_404_NOT_FOUND,
#                 'message': 'user topilmadi'
#             }
#             raise ValidationError(data)
#         user.delete()
#         data = {
#             'status': status.HTTP_204_NO_CONTENT,
#             'message': 'user topilmadi'
#         }
#         return Response(data)




#
# @api_view(['GET'])
# def get_info(request):
#     data = {
#         "success": True,
#         "message": "Hammasi joyida"
#     }
#     return Response(data)
#
# @api_view(['POST'])
# def create_product(request):
#     serializer = ProductSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         data = {
#             "success": True,
#             "message": "product yaratildi",
#             "data": serializer.data
#         }
#
#         return Response(data)
#     raise ValidationError(serializer.errors)
#
#
# @api_view(['get'])
# def list_product(request):
#     products = Product.objects.all()[::-1]
#     if len(products) == 0:
#         raise ValidationError("Malumot yo'q")
#
#     serializer = ProductSerializer(products, many=True)
#
#     data = {
#         "success": True,
#         "message": "products",
#         "data": serializer.data
#     }
#     return Response(data)
#
#
# @api_view(['GET'])
# def detail_product(request,pk):
#     products = Product.objects.filter(pk=pk).first()
#     if products is None:
#         raise ValidationError("Malumot Topilmadi")
#     serializer = ProductSerializer(products)
#
#     data = {
#         "success": True,
#         "message": "product",
#         "data": serializer.data
#     }
#     return Response(data)
#
#
# @api_view(['POST'])
# def update_product(request, pk):
#     products = Product.objects.filter(pk=pk).first()
#     if products is None:
#         raise ValidationError("Malumot Topilmadi")
#
#     serializer = ProductSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#
#         data = {
#             "success": True,
#             "message": "product yaratildi",
#             "data": serializer.data
#         }
#
#         return Response(data)
#     raise ValidationError(serializer.errors)
#
#
#
# @api_view(['PUTCH'])
# def putch_product(request, pk):
#     products = Product.objects.filter(pk=pk).first()
#     if products is None:
#         raise ValidationError("Malumot Topilmadi")
#
#     serializer = ProductSerializer(data = request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#
#         data = {
#             "success": True,
#             "message": "product yaratildi",
#             "data": serializer.data
#         }
#
#         return Response(data)
#     raise ValidationError(serializer.errors)
#
# @api_view(['DELETE',])
# def delete_product(request,pk):
#     product = Product.objects.filter(pk=pk).first()
#     if product is None:
#         raise ValidationError('Malumot topilmadi')
#     product.delete()
#     data = {
#             'success': True,
#             'massege': 'produc ochirildi',
#         }
#     return Response(data)
