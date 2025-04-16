from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Order


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order_detail(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

VALID_STATUSES = ['READY', 'IN_TRANSIT', 'DELIVERED', 'CANCELLED']

@api_view(['GET', 'PATCH'])
def order_status(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({
            'order_id': order.order_id,
            'status': order.status,
            'status_display': order.get_status_display()
        })

    elif request.method == 'PATCH':
        new_status = request.data.get('status')
        if new_status not in VALID_STATUSES:
            return Response(
                {'error': 'Invalid status. Use: READY, IN_TRANSIT, DELIVERED, CANCELLED'},
                status=status.HTTP_400_BAD_REQUEST
            )
        order.status = new_status
        order.save()
        return Response({
            'message': 'Status updated',
            'status': order.status,
            'status_display': order.get_status_display()
        })