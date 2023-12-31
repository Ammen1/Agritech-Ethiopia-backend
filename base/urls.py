from .views import SearchProduct, UpdateProduct, EditProduct, DeleteProduct, CreateProduct
from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('api/products/create/', CreateProduct.as_view(), name='create-product'),
    path('api/products/<int:pk>/update/',
         UpdateProduct.as_view(), name='update-product'),
    path('api/products/<int:pk>/delete/',
         DeleteProduct.as_view(), name='delete-product'),
    path('api/products/search/', SearchProduct.as_view(), name='search-product'),
    path('categories/', views.CategoryListCreateView.as_view(),
         name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(),
         name='category-detail'),
    path('product-types/', views.ProductTypeListCreateView.as_view(),
         name='producttype-list-create'),
    path('product-types/<int:pk>/', views.ProductTypeDetailView.as_view(),
         name='producttype-detail'),
]
