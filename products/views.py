from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Product, ProductSerializer
from rest_framework.exceptions import ValidationError
from .models import Product



@api_view(['GET'])
def get_info(request):
    data = {
        "success": True,
        "message": "Hammasi joyida"
    }
    return Response(data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            "success": True,
            "message": "product yaratildi",
            "data": serializer.data
        }

        return Response(data)
    raise ValidationError(serializer.errors)


@api_view(['get'])
def list_product(request):
    products = Product.objects.all()[::-1]
    if len(products) == 0:
        raise ValidationError("Malumot yo'q")

    serializer = ProductSerializer(products, many=True)

    data = {
        "success": True,
        "message": "products",
        "data": serializer.data
    }
    return Response(data)


@api_view(['GET'])
def detail_product(request,pk):
    products = Product.objects.filter(pk=pk).first()
    if products is None:
        raise ValidationError("Malumot Topilmadi")
    serializer = ProductSerializer(products)

    data = {
        "success": True,
        "message": "product",
        "data": serializer.data
    }
    return Response(data)


@api_view(['POST'])
def update_product(request, pk):
    products = Product.objects.filter(pk=pk).first()
    if products is None:
        raise ValidationError("Malumot Topilmadi")

    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

        data = {
            "success": True,
            "message": "product yaratildi",
            "data": serializer.data
        }

        return Response(data)
    raise ValidationError(serializer.errors)



@api_view(['PUTCH'])
def putch_product(request, pk):
    products = Product.objects.filter(pk=pk).first()
    if products is None:
        raise ValidationError("Malumot Topilmadi")

    serializer = ProductSerializer(data = request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

        data = {
            "success": True,
            "message": "product yaratildi",
            "data": serializer.data
        }

        return Response(data)
    raise ValidationError(serializer.errors)

@api_view(['DELETE',])
def delete_product(request,pk):
    product = Product.objects.filter(pk=pk).first()
    if product is None:
        raise ValidationError('Malumot topilmadi')
    product.delete()
    data = {
            'success': True,
            'massege': 'produc ochirildi',
        }
    return Response(data)
