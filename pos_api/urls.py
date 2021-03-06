
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=False)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products',include('product.urls')),
    path('api/',include('cart.urls')),
    path('api/customer/',include('customer.urls')),
    path('api/',include('order.urls')),
]
