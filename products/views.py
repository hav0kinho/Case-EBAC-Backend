from django.shortcuts import render


from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import AllowAny # Se der tempo, organizar
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self): # Sistema de Auth (Se testar, desativar)
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    
# Como ao meu ver é uma "abstração" dos produtos, ficará aqui
class PublicCatalogView(generics.ListAPIView):
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
