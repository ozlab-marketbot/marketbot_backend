from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    GET    /products/         → list all products
    POST   /products/         → create a new product
    GET    /products/{pk}/    → retrieve a single product
    PUT    /products/{pk}/    → update a product
    PATCH  /products/{pk}/    → partial update
    DELETE /products/{pk}/    → delete a product
    """
    queryset = Product.objects.all().order_by("-updated_at")
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # optional: enable filtering, searching, ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["external_vendor_code", "product_name", "category_code"]
    ordering_fields = ["sale_price", "stock_quantity", "updated_at"]
