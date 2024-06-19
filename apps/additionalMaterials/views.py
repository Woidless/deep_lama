# additionalMaterials/views.py
from rest_framework import generics, permissions
from .models import AdditionalMaterials
from .serializers import AdditionalMaterialsSerializer

class AdditionalMaterialsCreateView(generics.CreateAPIView):
    queryset = AdditionalMaterials.objects.all()
    serializer_class = AdditionalMaterialsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
