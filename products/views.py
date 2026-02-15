from django.core.serializers import serialize
from django.shortcuts import render ,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Product, ProductSerializer
from rest_framework.exceptions import ValidationError
from .models import Product
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, \
    UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError






class ProductListView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        data = {
            'status': status.HTTP_200_OK,
            'message': 'products',
            'data': serializer.data
        }
        return Response(data)

class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Products',
                'data': serializer.data
            }
            return Response(data)
        data = {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'error',
            'desc': serializer.errors
        }
        return Response(data)

class ProductUpdateView(APIView):
    def put(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'status': status.HTTP_200_OK,
            'message': 'product update',
            'data':serializer.data
        }
        return Response(data)

    def patch(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        serializer = ProductSerializer(product, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'status': status.HTTP_200_OK,
            'message': 'product update',
            'data':serializer.data
        }
        return Response(data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        data = {
            'status': status.HTTP_200_OK,
            'data': serializer.data
        }
        return Response(data)



class ProductDelateView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        data = {
            'status': status.HTTP_204_NO_CONTENT,
            'message': 'Product delete'
        }
        return Response(data)



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


# class ProductUpdateView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer









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
