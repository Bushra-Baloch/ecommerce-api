from rest_framework import filters
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import RegisterSerializer
from rest_framework import status


@api_view(['GET'])
def test_view(request):
    return Response({"message": "E-commerce API working ✅"})

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics, permissions

# List & Create

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

# Retrieve, Update, Delete
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]



from .models import CartItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    items = CartItem.objects.filter(user=request.user)
    serializer = CartItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += int(quantity)
    else:
        item.quantity = int(quantity)
    item.save()

    return Response({'message': 'Product added to cart'})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, product_id):
    try:
        item = CartItem.objects.get(user=request.user, product__id=product_id)
        item.delete()
        return Response({'message': 'Item removed from cart'})
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found in cart'}, status=404)


from .models import Order, OrderItem

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    if not cart_items.exists():
        return Response({"error": "Cart is empty"}, status=400)

    order = Order.objects.create(user=user)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    cart_items.delete()  # Empty cart after ordering

    return Response({"message": f"Order #{order.id} placed successfully!"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-ordered_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
