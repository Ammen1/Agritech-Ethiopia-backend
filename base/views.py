from rest_framework import generics, status
from django.db.models import Q
from django.shortcuts import get_object_or_404
from base.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ProductTypeSerializer
from .serializers import ProductSerializer
from .serializers import CategorySerializer
from .models import ProductType
from .models import Category
from .models import Product


class CreateProduct(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProduct(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EditProduct(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Post.objects.all()


class DeleteProduct(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SearchProduct(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        # Get the search query parameter from the URL
        query = self.request.query_params.get('q', '')
        category_id = self.request.query_params.get('category_id', '')

        # Create a filter for name and description search
        name_description_filter = (
            Q(name__icontains=query) |  # Search by product name
            Q(description__icontains=query)  # Search by product description
        )

        # Create a filter for category search
        category_filter = Q(category_id=category_id)

        # Combine the filters using OR condition
        queryset = Product.objects.filter(
            name_description_filter | category_filter)

        return queryset


# Category

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductTypeListCreateView(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def delete(self, request, *args, **kwargs):
        # Override the delete method to customize the response
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
