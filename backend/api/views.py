from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    authentication_classes = []
    permission_classes     = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data.get('name')
        quantity = data.get('quantity', 0)

        if not name or not str(quantity).isdigit():
            return Response({"detail": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            item = Item.objects.get(name=name)
            item.quantity += int(quantity)
            item.save()
            serializer = ItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            # Create a new item
            return super().create(request, *args, **kwargs)