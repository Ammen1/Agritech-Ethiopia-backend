from django.shortcuts import get_object_or_404
from base.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Product
from .serializers import ProductSerializer


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

        # Perform the search using the Q objects and filtering
        return Product.objects.filter(
            Q(name__icontains=query) |  # Search by product name
            Q(description__icontains=query)  # Search by product description
        )
