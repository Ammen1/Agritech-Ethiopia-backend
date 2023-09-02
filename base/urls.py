from .views import SearchProduct, UpdateProduct, EditProduct, DeleteProduct, CreateProduct
from django.urls import path

app_name = 'base'

urlpatterns = [
    path('api/products/create/', CreateProduct.as_view(), name='create-product'),
    path('api/products/<int:pk>/update/',
         UpdateProduct.as_view(), name='update-product'),
    path('api/products/<int:pk>/delete/',
         DeleteProduct.as_view(), name='delete-product'),
    path('api/products/search/', SearchProduct.as_view(), name='search-product'),
]
