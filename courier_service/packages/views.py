import uuid
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Package
from .serializers import PackageSerializer, PackageLookupSerializer  # Import the custom serializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.filter(deleted_at__isnull=True)
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        tracking_number = str(uuid.uuid4())  # Generate a unique tracking number
        serializer.save(sender=self.request.user, tracking_number=tracking_number)

    @action(detail=True, methods=['delete'])
    def soft_delete(self, request, pk=None):
        package = self.get_object()
        package.soft_delete()
        return Response({'message': 'Package soft deleted'}, status=200)

    @action(detail=True, methods=['post'])
    def restore(self, request, pk=None):
        package = Package.objects.get(id=pk, deleted_at__isnull=False)
        package.restore()
        return Response({'message': 'Package restored'}, status=200)

    @action(detail=False, methods=['post'])
    def get_package_by_tracking(self, request):
        tracking_number = request.data.get('tracking_number')
        if not tracking_number:
            return Response({'detail': 'Tracking number is required'}, status=400)

        try:
            package = Package.objects.get(tracking_number=tracking_number, deleted_at__isnull=True)
            serializer = PackageLookupSerializer(package)  # Use the custom serializer
            return Response(serializer.data, status=200)
        except Package.DoesNotExist:
            return Response({'detail': 'Package not found'}, status=404)
