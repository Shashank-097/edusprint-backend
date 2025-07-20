from rest_framework import viewsets
from .models import ServiceCategory
from .serializers import ServiceCategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
  