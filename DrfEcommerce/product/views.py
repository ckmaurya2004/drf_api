from django.shortcuts import render,HttpResponse
from drf_spectacular.utils import extend_schema
from . models import *
from . serializer import *
from rest_framework import serializers,viewsets
from rest_framework.serializers import ValidationError
from rest_framework .response import Response
from rest_framework.decorators import action



# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

     
    @extend_schema(request=CategorySerializer)
    def list(self,request):
        serializer = CategorySerializer(self.queryset,many = True)
        return Response(serializer.data)
   
class ProductViewSet(viewsets.ViewSet):
   
    queryset = Product.objects.all()
    @action(detail=False,
            methods=['get'],
            url_path= r'category/(?P<category>[^/]+)/all'
            )
    def list_product_by_category(self, request,category=None):
        serialized = ProductSerializer(self.queryset.filter(category__name=category),many = True)
        return Response(serialized.data)
    
    serializer_class = ProductSerializer
    @extend_schema(request=ProductSerializer)
    def list(self,request):
        serializer = ProductSerializer(self.queryset,many = True)
        return Response(serializer.data)
   

class BrandViewSet(viewsets.ViewSet):
    serializer_class = BrandSerializer
    
    queryset = Brand.objects.all()
    @extend_schema(request=BrandSerializer)
    def list(self,request):
        serializer = BrandSerializer(self.queryset,many = True)
        return Response(serializer.data)
   


