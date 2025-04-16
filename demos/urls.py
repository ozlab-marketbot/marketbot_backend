from django.urls import path
from .views import order_list, order_detail, create_order, order_status

urlpatterns = [
    path('', order_list),  # GET /orders/
    path('create/', create_order),  # POST /orders/create/
    path('<str:order_id>/', order_detail),  # GET /orders/<order_id>/
    path('<str:order_id>/status/', order_status),  # GET or PATCH /orders/<order_id>/status/
]
