from django.urls import path
from .views import HomeView, checkout, product

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/', product, name='product'),
]