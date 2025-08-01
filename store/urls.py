from django.urls import path
from .views import test_view,register_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProductListCreateView, ProductDetailView
from .views import view_cart, add_to_cart, remove_from_cart
from .views import place_order, user_orders

urlpatterns = [
    path('test/', test_view),
    path('register/', register_user),  # signup
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', view_cart),
    path('cart/add/', add_to_cart),
    path('cart/remove/<int:product_id>/', remove_from_cart),
     path('orders/place/', place_order),
    path('orders/my/', user_orders),
]